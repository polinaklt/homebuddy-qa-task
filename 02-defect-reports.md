# Defect Reports

---

## DEF-02: "Not sure" on kitchen size step returns the user to the same question, the user can't continue without entering a size

**Severity:** Critical

**Environment:**

- Browser: Chrome Version 156.0.8078.48 (Official Build) (arm64), macOS

**Steps to reproduce:**

1. Open <https://hb-test.stage.sirenltd.dev/>
2. Enter ZIP `10001`, click "Get estimate".
3. Select "Kitchen cabinets", click "Next".
4. Select "Replace all or most cabinets", click "Next".
5. Select "Single family home", click "Next".
6. Select "No" for "Is it a mobile, modular or manufactured home?", click "Next".
7. Select "Yes" for "Are you the homeowner or authorized to make property changes?", click "Next".
8. On "What is the approximate size of your kitchen in square feet?" leave the size field empty and check "Not sure".
9. Click "Next". Repeat a few times.

**Expected result:** The wizard moves to the budget step ("Do you know what your approximate budget is?").

**Actual result:** The same kitchen size question is shown again after every click on "Next". The user can't continue without entering a size. Every click sends `PUT /v1/public/leads/{id}` with body `{"squareFeet":null,"notSure":"yes"}`, response `200`.

**Attachments:** [screen recording](screenshots/DEF-2_recording_1.mov)

---

## DEF-04: Budget answer is not saved: API returns 422, UI ignores the error and continues

**Severity:** High

**Environment:**

- Browser: Chrome Version 156.0.8078.48 (Official Build) (arm64), macOS

**Steps to reproduce:**

1. Open <https://hb-test.stage.sirenltd.dev/>
2. Enter ZIP `10001`, click "Get estimate".
3. Select "Kitchen cabinets", click "Next".
4. Select "Replace all or most cabinets", click "Next".
5. Select "Single family home", click "Next".
6. Select "No" for "Is it a mobile, modular or manufactured home?", click "Next".
7. Select "Yes" for "Are you the homeowner or authorized to make property changes?", click "Next".
8. On the kitchen size step enter `200`, click "Next".
9. On "Do you know what your approximate budget is?" select "$10K to $30K".
10. Click "Next".
11. Check the `PUT /v1/public/leads/{id}` request in Network.

**Expected result:** The selected budget is saved (`2xx` response) with a value that matches "$10K to $30K". If saving fails, the user sees an error and stays on the step.

**Actual result:**

- Request body: `{"budget":"2"}`
- Response: `422 Unprocessable Entity`
- Response body: `{"errors":{"budget":[{"code":"budget_enum","message":"The selected budget is invalid."}]}}`
- The error is ignored and the next step is open ("Who should I prepare this estimate for?").

**Additional notes:** "$5K to $10K", "$10K to $30K", "More than $30K" and "Not sure" options have the same `value="2"`. Only "Up to $5K" has `value="1"`. The backend couldn't tell these answers apart if the request succeeded. (DEF-06)

**Attachments:** [screen recording](screenshots/DEF-4_recording-1.mov)

---

## DEF-05: Thank-you page shows "Andrew" instead of the name entered by the user

**Severity:** High

**Environment:**

- Browser: Chrome Version 156.0.8078.48 (Official Build) (arm64), macOS

**Steps to reproduce:**

1. Open <https://hb-test.stage.sirenltd.dev/>
2. Enter ZIP `10001`, click "Get estimate".
3. Select "Kitchen cabinets", click "Next".
4. Select "Replace all or most cabinets", click "Next".
5. Select "Single family home", click "Next".
6. Select "No" for "Is it a mobile, modular or manufactured home?", click "Next".
7. Select "Yes" for "Are you the homeowner or authorized to make property changes?", click "Next".
8. On the kitchen size step enter `200`, click "Next".
9. On "Do you know what your approximate budget is?" select "$10K to $30K", click "Next".
10. On "Who should I prepare this estimate for?" enter full name `Polina Test` and email `polina.test+n@example.com`, click "Next" (use a new email for each run: the site blocks a repeated phone + email pair).
11. Enter phone `3125550111`, click "Submit my request".
12. On the confirmation screen click "Phone number is correct".

**Expected result:** The thank-you page uses the entered name: "Thank you Polina, ...".

**Actual result:** The page says "Thank you Andrew, your contractor QA company will call soon!"

`GET /v1/public/leads/{id}` on the thank-you page returns `"fullName":"Polina Test"`. The API data is correct, so the name is hardcoded or taken from the wrong field on the front end.

**Attachments:** [entered name](screenshots/DEF-5_Screenshot_1.png), [thank-you page and GET response](screenshots/DEF-5_Screenshot_2.png)
