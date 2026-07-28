# Day 4 – Zero-shot, One-shot & Few-shot Prompting

## Objective

Learn how examples improve AI performance by comparing Zero-shot, One-shot, Three-shot, and Five-shot prompting.

---

# Dataset

| Message | Category |
|---------|----------|
| The app crashes whenever I open it. | Bug |
| How do I change my password? | Question |
| Excellent customer support! | Praise |
| My order arrived two days late. | Complaint |
| I can't upload my profile picture. | Bug |
| Where can I download my invoice? | Question |
| The new update is fantastic! | Praise |
| The website is very slow today. | Complaint |
| The login button does nothing. | Bug |
| Can I cancel my subscription? | Question |

---

# Zero-Shot Prompt

Classify each customer support message into one of these categories:

- Bug
- Question
- Praise
- Complaint

Messages:

1. The app crashes whenever I open it.
2. How do I change my password?
3. Excellent customer support!
4. My order arrived two days late.
5. I can't upload my profile picture.
6. Where can I download my invoice?
7. The new update is fantastic!
8. The website is very slow today.
9. The login button does nothing.
10. Can I cancel my subscription?

Return only the message number and its category.

## AI Response
<img width="1229" height="764" alt="image" src="https://github.com/user-attachments/assets/290c1757-dc87-44e2-a1d1-325db8e43bba" />

---

# One-Shot Prompt

Classify each customer support message into one of these categories:

- Bug
- Question
- Praise
- Complaint

Example:

"The app crashes after I log in." → Bug

Now classify these messages:

1. The app crashes whenever I open it.
2. How do I change my password?
3. Excellent customer support!
4. My order arrived two days late.
5. I can't upload my profile picture.
6. Where can I download my invoice?
7. The new update is fantastic!
8. The website is very slow today.
9. The login button does nothing.
10. Can I cancel my subscription?

Return only the message number and its category.

## AI Response
<img width="1323" height="731" alt="image" src="https://github.com/user-attachments/assets/f2d5acf2-b171-4319-8264-55efd6ed55a5" />

---

# Three-Shot Prompt

Classify each customer support message into one of these categories:

- Bug
- Question
- Praise
- Complaint

Examples:

"The app crashes after I log in." → Bug

"How can I reset my password?" → Question

"Your service is amazing!" → Praise

Now classify these messages:

1. The app crashes whenever I open it.
2. How do I change my password?
3. Excellent customer support!
4. My order arrived two days late.
5. I can't upload my profile picture.
6. Where can I download my invoice?
7. The new update is fantastic!
8. The website is very slow today.
9. The login button does nothing.
10. Can I cancel my subscription?

Return only the message number and its category.

## AI Response
<img width="1143" height="707" alt="image" src="https://github.com/user-attachments/assets/d9afe7a6-18a4-4707-8690-27ca146620df" />

---

# Five-Shot Prompt

Classify each customer support message into one of these categories:

- Bug
- Question
- Praise
- Complaint

Examples:

"The app crashes after I log in." → Bug

"How can I reset my password?" → Question

"Your service is amazing!" → Praise

"My package arrived damaged." → Complaint

"The login page won't load." → Bug

Now classify these messages:

1. The app crashes whenever I open it.
2. How do I change my password?
3. Excellent customer support!
4. My order arrived two days late.
5. I can't upload my profile picture.
6. Where can I download my invoice?
7. The new update is fantastic!
8. The website is very slow today.
9. The login button does nothing.
10. Can I cancel my subscription?

Return only the message number and its category.

## AI Response
<img width="1265" height="764" alt="image" src="https://github.com/user-attachments/assets/32237e50-caec-4eb5-98ff-0f6e5cd5f80e" />

---

# Wrong Example Prompt

Classify each customer support message into one of these categories:

- Bug
- Question
- Praise
- Complaint

Examples:

"The app crashes after I log in." → Praise

"How can I reset my password?" → Question

"Your service is amazing!" → Praise

Now classify these messages:

1. The app crashes whenever I open it.
2. How do I change my password?
3. Excellent customer support!
4. My order arrived two days late.

Return only the message number and its category.

## AI Response
<img width="1230" height="754" alt="image" src="https://github.com/user-attachments/assets/821c5cb2-34af-4b78-855b-63fd05d4d820" />

---

# Results

| Prompt Type | Accuracy |
|-------------|----------|
| Zero-shot | 10/10 |
| One-shot | 10/10 |
| Three-shot | 10/10 |
| Five-shot | 10/10 |

---

# Observation

The intentionally incorrect example reduced the quality of the model's predictions. This demonstrated that poor examples can negatively influence the AI's behavior.

---

# Conclusion

For this task, One-shot and Three-shot prompting were sufficient to achieve accurate classifications. Adding more examples did not significantly improve performance, while incorrect examples degraded the quality of the output.
