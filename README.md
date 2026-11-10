# QA Test Task: HomeBuddy Kitchen Remodeling

Target: <https://hb-test.stage.sirenltd.dev/> (landing page and lead wizard)

## Contents

1. [Defect list by severity](01-defects-list.md)
2. [Defect reports](02-defect-reports.md)
3. [Product questions](03-product-questions.md)
4. [Test suite structure](04-test-suite.md)
5. [Test cases](05-test-cases.md)
6. [Automation](#automation)

## Notes

- Requirements were not provided. Expected behavior is based on the page content and common practice for lead forms.

## Automation

### Test cases with the highest ROI

| Test case | Why |
|---|---|
| TC-01 Submit a lead (happy path) | Main business flow, must pass on every release. One run covers ZIP, all wizard steps and submission |
| TC-02 ZIP validation | One field, many inputs. Easy to parametrize, fast and stable. ZIP is the entry point for every lead |
| TC-10 Lead data in the API | Checks that the lead is really saved, not only that the UI shows success. Silent data loss (DEF-01) is easy to miss manually |

### Automated test

TC-01 with the API check from TC-10: [tests/test_lead_happy_path.py](tests/test_lead_happy_path.py). Locators are in [tests/locators.py](tests/locators.py).

Expected result of a run:

- `test_thank_you_page_is_shown`: passed
- `test_thank_you_page_shows_entered_name`: xfailed, known DEF-05
- `test_lead_status_is_submitted`: xfailed, known DEF-01 (passes on runs where DEF-01 does not reproduce)

### How to run

Chrome must be installed.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest -v
```
