
from hypothesis import given, settings, strategies as st
from scholarship_awards import parse_applicant, marks_average, payable_award


@given(st.one_of(st.text(), st.none(), st.integers()))
@settings(max_examples=100)
def test_parse_applicant_no_crash(s):
    try:
        parse_applicant(s)
    except Exception as e:
        assert False, f"parse_applicant crashed with {s!r}: {e}"


@given(st.one_of(st.text(), st.none(), st.integers()))
@settings(max_examples=100)
def test_marks_average_no_crash(s):
    try:
        marks_average(s)
    except Exception as e:
        assert False, f"marks_average crashed with {s!r}: {e}"


@given(st.one_of(st.text(), st.none(), st.integers()))
@settings(max_examples=100)
def test_payable_award_no_crash(s):
    try:
        payable_award(s)
    except Exception as e:
        assert False, f"payable_award crashed with {s!r}: {e}"
