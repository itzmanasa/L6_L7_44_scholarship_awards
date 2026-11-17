
"""Fixed Scholarship Awards application."""


def parse_applicant(text):
    if not isinstance(text, str):
        return None

    parts = text.split(':')
    if len(parts) != 2:
        return None

    category = parts[0].strip()
    marks_text = parts[1].strip()

    if not category or not marks_text:
        return None

    try:
        marks = float(marks_text)
    except (ValueError, TypeError):
        return None

    return category.title(), marks


def marks_average(marks_csv):
    if not isinstance(marks_csv, str):
        return None

    try:
        values = [int(r.strip()) for r in marks_csv.split(',')]
        if not values:
            return None
        return sum(values) // len(values)
    except (ValueError, TypeError, ZeroDivisionError):
        return None


def payable_award(text):
    if not isinstance(text, str):
        return None

    parts = text.split('|')
    if len(parts) != 2:
        return None

    try:
        award = float(parts[0].strip())
        deduction = float(parts[1].strip())
    except (ValueError, TypeError):
        return None

    return max(award * 1.18 - deduction, 0)


def main():
    print("==== Running parse_applicant ====")
    user_input = input("Enter category:marks (e.g. merit:82): ")
    print("Category and Marks:", parse_applicant(user_input))

    print("\n==== Running marks_average ====")
    user_input = input("Enter marks as CSV (e.g. 72,85,90): ")
    print("Average Marks:", marks_average(user_input))

    print("\n==== Running payable_award ====")
    user_input = input("Enter award|deduction (e.g. 5000|500): ")
    print("Payable Award:", payable_award(user_input))


if __name__ == "__main__":
    main()
