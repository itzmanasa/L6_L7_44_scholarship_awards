
import pytest

from scholarship_awards import (
    award_amount,
    is_eligible,
    application_status
)


# ==========================================
# 1. AWARD AMOUNT - BRANCH COVERAGE
# ==========================================

def test_invalid_category_branch():
    with pytest.raises(ValueError, match="unknown category"):
        award_amount("science", 90, "low", False)


def test_valid_category_branch():
    assert award_amount("merit", 80, "low", False) == 500


def test_negative_marks_branch():
    with pytest.raises(ValueError, match="invalid marks"):
        award_amount("merit", -1, "low", False)


def test_non_negative_marks_branch():
    assert award_amount("merit", 80, "low", False) == 500


def test_renewal_true_non_sports():
    assert award_amount("merit", 71, "low", True) == 100


def test_renewal_false():
    assert award_amount("merit", 80, "low", False) == 500


def test_renewal_true_sports_exception():
    assert award_amount("sports", 60, "low", True) == 0


def test_above_cutoff_branch():
    assert award_amount("arts", 70, "low", False) == 500


def test_at_cutoff_branch():
    assert award_amount("arts", 65, "low", False) == 0


def test_below_cutoff_branch():
    assert award_amount("merit", 70, "low", False) == 0


def test_low_income_rate():
    assert award_amount("merit", 80, "low", False) == 500


def test_high_income_rate():
    assert award_amount("merit", 80, "high", False) == 300


def test_above_15_low_income():
    assert award_amount("merit", 91, "low", False) == 2560


def test_above_15_high_income():
    assert award_amount("merit", 91, "high", False) == 1600


def test_exactly_15_above_cutoff():
    assert award_amount("merit", 90, "low", False) == 1500


# ==========================================
# 2. ELIGIBILITY - BRANCH COVERAGE
# ==========================================

def test_special_quota_with_two_backlogs():
    assert is_eligible(50, 2, True) is True


def test_special_quota_with_more_than_two_backlogs():
    assert is_eligible(90, 3, True) is False


def test_normal_quota_attendance_below_75():
    assert is_eligible(74, 0, False) is False


def test_normal_quota_attendance_equal_to_75():
    assert is_eligible(75, 1, False) is True


def test_normal_quota_attendance_above_75():
    assert is_eligible(90, 0, False) is True


def test_normal_quota_one_backlog():
    assert is_eligible(90, 1, False) is True


def test_normal_quota_more_than_one_backlog():
    assert is_eligible(90, 2, False) is False


# ==========================================
# 3. APPLICATION STATUS - BRANCH COVERAGE
# ==========================================

def test_new_application_open():
    assert application_status(20, False, False) == "open"


def test_new_application_closing():
    assert application_status(5, False, False) == "closing"


def test_new_application_closed():
    assert application_status(4, False, False) == "closed"


def test_renewal_application_open():
    assert application_status(30, True, False) == "open"


def test_renewal_application_closing():
    assert application_status(15, True, False) == "closing"


def test_renewal_application_closed():
    assert application_status(14, True, False) == "closed"


def test_paper_application_open():
    assert application_status(30, False, True) == "open"


def test_paper_application_closing():
    assert application_status(15, False, True) == "closing"


def test_paper_application_closed():
    assert application_status(14, False, True) == "closed"


def test_renewal_paper_application_open():
    assert application_status(40, True, True) == "open"


def test_renewal_paper_application_closing():
    assert application_status(25, True, True) == "closing"


def test_renewal_paper_application_closed():
    assert application_status(24, True, True) == "closed"
