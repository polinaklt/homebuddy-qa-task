# Test Cases

Environment: <https://hb-test.stage.sirenltd.dev/>, Chrome, desktop.

---

## TC-01: Submit a lead with valid data (happy path)

**Priority:** Critical | **Type:** E2E

**Preconditions:** Landing page is open.

**Test data:** ZIP `10001`, full name `Polina Test`, email `polina.test+<unique>@example.com` (new for each run, the site blocks a repeated phone + email pair), phone `3125550111`, kitchen size `200`

| # | Step | Expected result |
|---|---|---|
| 1 | Enter ZIP, click "Get estimate" | Wizard opens on the first question |
| 2 | Select "Kitchen cabinets", click "Next" | Cabinets question is shown |
| 3 | Select "Replace all or most cabinets", click "Next" | Property type question is shown |
| 4 | Select "Single family home", click "Next" | Mobile home question is shown |
| 5 | Select "No", click "Next" | Homeowner question is shown |
| 6 | Select "Yes", click "Next" | Kitchen size question is shown |
| 7 | Enter kitchen size, click "Next" | Budget question is shown |
| 8 | Select "$10K to $30K", click "Next" | Contact step is shown |
| 9 | Enter full name and email, click "Next" | Phone step is shown |
| 10 | Enter phone, click "Submit my request" | Phone confirmation screen or thank-you page is shown |
| 11 | Click "Phone number is correct" (if shown) | Thank-you page opens: "Thank you Polina, ..." |

**Known issues:** DEF-05, DEF-01

---

## TC-02: ZIP Code validation with invalid values

**Priority:** High | **Type:** Negative

**Preconditions:** Landing page is open.

**Test data:** See the table

**Steps:** Enter the value, click "Get estimate".

| # | Input | Expected result |
|---|---|---|
| 1 | `1234` | Error "The ZIP Code must be 5 digits with no spaces" |
| 2 | `123456` | Field does not accept the 6th digit |
| 3 | `abcde` | Format error |
| 4 | `12 34` | Format error |
| 5 | empty | Error message |

For all rows the wizard does not open.

**Known issues:** DEF-14, DEF-15

---

## TC-03: Out-of-area ZIP

**Priority:** High | **Type:** Functional

**Preconditions:** Landing page is open.

**Test data:** Out-of-area ZIP `90210`, in-area ZIP `10001`

| # | Step | Expected result |
|---|---|---|
| 1 | Enter ZIP `90210`, click "Get estimate" | Screen "Unfortunately, I have no matching contractors in your area yet." |
| 2 | Click "Try another ZIP Code" | Landing page with an empty ZIP field |
| 3 | Enter ZIP `10001`, click "Get estimate" | Wizard opens |

---

## TC-04: "Not sure" on kitchen size step

**Priority:** High | **Type:** Functional

**Preconditions:** Landing page is open. Enter ZIP `10001`, click "Get estimate" and answer the wizard with the answers from Test data until the kitchen size step.

**Test data:** ZIP `10001`; Kitchen cabinets, Replace all or most cabinets, Single family home, mobile home No, homeowner Yes

| # | Step | Expected result |
|---|---|---|
| 1 | Leave the size empty, check "Not sure" | "Next" is enabled |
| 2 | Click "Next" | Budget question is shown |

**Known issue:** DEF-02

---

## TC-05: Budget is saved for each option

**Priority:** High | **Type:** API

**Preconditions:** DevTools > Network is open. Landing page is open. Enter ZIP `10001`, click "Get estimate" and answer the wizard with the answers from Test data until the budget step.

**Test data:** ZIP `10001`; Kitchen cabinets, Replace all or most cabinets, Single family home, mobile home No, homeowner Yes, size `200`; budget options from the table

**Steps:** Select the option, click "Next", check `PUT /v1/public/leads/{id}`. Repeat for each option in a new session.

| # | Option | Expected result |
|---|---|---|
| 1 | Up to $5K | Response `2xx`, value unique for this option |
| 2 | $5K to $10K | Same |
| 3 | $10K to $30K | Same |
| 4 | More than $30K | Same |
| 5 | Not sure | Option can be selected, same |

If the API returns an error, the user stays on the step and sees a message.

**Known issues:** DEF-04, DEF-06, DEF-03

---

## TC-06: Cabinets question depends on the selected elements

**Priority:** Medium | **Type:** Functional

**Preconditions:** Landing page is open.

**Test data:** ZIP `10001`; elements "Countertop(s)" (run 1), "Kitchen cabinets" (run 2)

| # | Step | Expected result |
|---|---|---|
| 1 | Enter ZIP, select "Countertop(s)" only, click "Next" | Cabinets question is skipped, property type question is shown |
| 2 | Start again, select "Kitchen cabinets", click "Next" | "What would you like to do with your kitchen cabinets?" is shown |

---

## TC-07: Commercial property warning

**Priority:** Medium | **Type:** Functional

**Preconditions:** Landing page is open. Enter ZIP `10001`, click "Get estimate" and answer the wizard with the answers from Test data until the property type step.

**Test data:** ZIP `10001`; Kitchen cabinets, Replace all or most cabinets; property type "Commercial"

| # | Step | Expected result |
|---|---|---|
| 1 | Select "Commercial" | Warning "Our contractors only work with single or multi-family homes. Would you still like to continue?" |
| 2 | Click "No" | Page "Sorry to see you go!" |
| 3 | Start again, select "Commercial", click "Yes" | Next question is shown |

---

## TC-08: Full name validation

**Priority:** Medium | **Type:** Negative, Boundary

**Preconditions:** Landing page is open. Enter ZIP `10001`, click "Get estimate" and answer the wizard with the answers from Test data until the contact step ("Who should I prepare this estimate for?").

**Test data:** ZIP `10001`; Kitchen cabinets, Replace all or most cabinets, Single family home, mobile home No, homeowner Yes, size `200`, budget $10K to $30K; email `polina.test+<unique>@example.com`; full names from the table

| # | Full name | Expected result |
|---|---|---|
| 1 | `Polina Tes` (10 characters) | Accepted |
| 2 | `Polina Te` (9 characters) | Error "Full name must be at least 10 characters." |
| 3 | `Polinatest` (one word) | Error: first and last name are required |
| 4 | `Полина Тест` (Cyrillic) | Error "Full name must be written in English letters..." |
| 5 | `Polina Test-Smith` (dash) | Accepted |

**Known issue:** DEF-10

---

## TC-09: Phone confirmation screen

**Priority:** Medium | **Type:** Functional

**Preconditions:** Landing page is open. Enter ZIP `10001`, click "Get estimate", answer the wizard with the answers from Test data, enter full name and email, click "Next". The phone step is shown.

**Test data:** ZIP `10001`; Kitchen cabinets, Replace all or most cabinets, Single family home, mobile home No, homeowner Yes, size `200`, budget $10K to $30K; full name `Polina Test`, email `polina.test+<unique>@example.com`; phone `3125550111`, then `3125550122` after "Edit phone number"

| # | Step | Expected result |
|---|---|---|
| 1 | Enter `3125550111`, click "Submit my request" | Screen "Please confirm your phone number." with the entered number |
| 2 | Click "Edit phone number" | Phone step with the entered number, it can be changed |
| 3 | Change to `3125550122`, submit, click "Phone number is correct" | Thank-you page opens |

---

## TC-10: Lead data in the API matches the entered data

**Priority:** High | **Type:** UI + API

**Preconditions:** Landing page is open, DevTools > Network is open.

**Test data:** ZIP `10001`; Kitchen cabinets, Replace all or most cabinets, Single family home, mobile home No, homeowner Yes, size `200`, budget $10K to $30K; full name `Polina Test`, email `polina.test+<unique>@example.com`, phone `3125550111`

| # | Step | Expected result |
|---|---|---|
| 1 | Enter ZIP, click "Get estimate" | Wizard opens |
| 2 | Answer the wizard with the answers from Test data | Contact step is shown |
| 3 | Enter full name and email, click "Next" | Phone step is shown |
| 4 | Enter phone, click "Submit my request", click "Phone number is correct" (if shown) | Thank-you page opens |
| 5 | Check `GET /v1/public/leads/{id}` in Network | `fullName: "Polina Test"`, `zipCode: "10001"`, `phoneNumber: "3125550111"`, `leadStatus: "SUBMITTED"` |
| 6 | Compare with the thank-you page | The name on the page matches `fullName` |

**Known issues:** DEF-05, DEF-01
