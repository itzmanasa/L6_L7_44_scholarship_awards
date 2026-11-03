import pytest

from scholarship_awards import (
    award_amount,
    is_eligible,
    application_status
)


# -------------------------------
# AWARD AMOUNT TESTS
# -------------------------------

def test_invalid_category():
    with pytest.raises(ValueError, match="unknown category"):
        award_amount("science", 90, "low", False)


def test_negative_marks():
    with pytest.raises(ValueError, match="invalid marks"):
        award_amount("merit", -5, "low", False)


def test_marks_equal_to_cutoff():
    assert award_amount("merit", 75, "low", False) == 0


def test_marks_below_cutoff():
    assert award_amount("merit", 70, "low", False) == 0


def test_low_income_normal_award():
    assert award_amount("merit", 80, "low", False) == 500


def test_high_income_normal_award():
    assert award_amount("merit", 80, "high", False) == 300


def test_low_income_bonus_award():
    assert award_amount("merit", 91, "low", False) == 2560


def test_high_income_bonus_award():
    assert award_amount("merit", 91, "high", False) == 1600


def test_renewal_reduces_cutoff():
    assert award_amount("arts", 65, "low", True) == 500


def test_sports_renewal_does_not_reduce_cutoff():
    assert award_amount("sports", 60, "low", True) == 0


# -------------------------------
# ELIGIBILITY TESTS
# -------------------------------

def test_special_quota_eligible():
    assert is_eligible(50, 2, True) is True


def test_special_quota_ineligible():
    assert is_eligible(90, 3, True) is False


def test_normal_quota_low_attendance():
    assert is_eligible(74, 0, False) is False


def test_normal_quota_eligible():
    assert is_eligible(75, 1, False) is True


def test_normal_quota_too_many_backlogs():
    assert is_eligible(90, 2, False) is False


# -------------------------------
# APPLICATION STATUS TESTS
# -------------------------------

def test_new_application_open():
    assert application_status(20, False, False) == "open"


def test_new_application_closing():
    assert application_status(5, False, False) == "closing"


def test_new_application_closed():
    assert application_status(4, False, False) == "closed"


def test_renewal_application_open():
    assert application_status(30, True, False) == "open"


def test_renewal_paper_application_open():
    assert application_status(40, True, True) == "open"


def test_renewal_paper_application_closing():
    assert application_status(25, True, True) == "closing"


def test_renewal_paper_application_closed():
    assert application_status(24, True, True) == "closed"