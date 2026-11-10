# Defect List

Questions that need a product decision are in [03-product-questions.md](03-product-questions.md).

| ID | Severity | Area | Summary |
|---|---|---|---|
| DEF-01 | Critical | Submission, thank-you page | Thank-you page "your contractor QA company will call soon!" is shown, but the lead has `"leadStatus": "FAILED"` in `GET /v1/public/leads/{id}`. The user thinks the request was sent, the contractor never gets it. Not reproduced on Nov 9 (same data, status SUBMITTED), first noticed on Nov 10 |
| DEF-02 | Critical | Wizard, kitchen size | "Not sure" without a size returns the user to the same question on every "Next". The user can't continue without entering a size |
| DEF-03 | High | Wizard, budget | "Not sure" option on the budget step can't be selected, "Next" stays disabled. A user who doesn't know the budget can continue only by picking a range |
| DEF-04 | High | API, budget | Budget is never saved: `PUT /v1/public/leads/{id}` returns `422 budget_enum` for every option, UI ignores the error and continues |
| DEF-05 | High | Thank-you page | Page says "Thank you Andrew" instead of the entered name. API returns the correct `fullName` |
| DEF-06 | High | Wizard, budget | "$5K to $10K", "$10K to $30K", "More than $30K" and "Not sure" budget options have the same `value="2"` |
| DEF-07 | Medium | Footer | "Terms Of Use" link opens /privacy-policy |
| DEF-08 | Medium | Wizard, kitchen size | Size and "Not sure" can be set at the same time |
| DEF-09 | Medium | Wizard, navigation | No "Back" button. To change an answer the user has to close the wizard and start again |
| DEF-10 | Medium | Wizard, contact step | Full name validation is inconsistent: 0-1 letters shows "at least 10 characters", 2+ letters shows "English letters" error, two short words under 10 characters pass |
| DEF-11 | Medium | Landing content | Kitchen page contains a roofing section "Benefits Of Asphalt Shingles" |
| DEF-12 | Medium | Landing page | Console error on load: "Uncaught Error: This is a mistake, you can create a bug report on this." |
| DEF-13 | Medium | Privacy Policy | No header, logo or link back to the landing page |
| DEF-14 | Low | ZIP form | Empty ZIP: click on "Get estimate" does nothing, no error message |
| DEF-15 | Low | ZIP form | ZIP field has no max length and accepts letters. Validation on submit catches it, but the input should be limited to 5 digits |
| DEF-16 | Low | Footer | Footer shows future year and no company name "© 2027." |
| DEF-17 | Low | Reviews | Bradley C. review links to remodelusallc.com/about-us/testimonials/ (404) |
| DEF-18 | Low | Landing content | "Materials warranty[1]" has a footnote marker, no footnote text on the page |
| DEF-19 | Low | Landing content | "The kitchen is ‘the heart of the home for a reason": no closing quote |
| DEF-20 | Low | Landing content | Typos: "thay look and work great", "wher professional" |
| DEF-21 | Low | Wizard, kitchen size | Field accepts any value up to 5 digits (99999 sq ft), no range check |
| DEF-22 | Low | Attributes | Duplicate `data-autotest` attributes (budget radios, kitchen elements) |
