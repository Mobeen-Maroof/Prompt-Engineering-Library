# Day 6 – Reliability: Stopping Hallucinations & Iterating Like a Pro

## Objective

Learn how to reduce hallucinations using grounding and permission to abstain, and improve prompts through structured iteration.

---

# Exercise 1 – Hallucination

## Original Prompt

What was TechNova Solutions' revenue in Q3 2025, and what were the main reasons for the increase in revenue?

### AI Response
<img width="1217" height="744" alt="image" src="https://github.com/user-attachments/assets/fbe6d19c-a18b-4a0a-b492-2b259c6dcb56" />
<img width="1204" height="452" alt="image" src="https://github.com/user-attachments/assets/5557ee28-b500-4a6d-a0cb-9439e21ab2d3" />

---

# Improved Prompt

Using ONLY the report below, answer the question.

If the answer is not clearly mentioned, respond with:

"Not stated in the document."

Report:

TechNova Solutions published its annual internship recruitment announcement.

The company is hiring Software Engineer Interns in Karachi.

Applications close on August 15, 2026.

Question:

What was TechNova Solutions' revenue in Q3 2025, and what caused the increase?

### AI Response
<img width="1345" height="707" alt="image" src="https://github.com/user-attachments/assets/24088628-d2ac-4226-9810-97d879cb6f22" />

---

# Observation

The improved prompt prevented unsupported claims by grounding the model in the provided text and allowing it to say that the information was not available.

---

# Original Prompt 

Give me some project ideas.

### AI Response
<img width="1167" height="761" alt="image" src="https://github.com/user-attachments/assets/a25c8fed-a43f-4863-9f47-ba2bca87a927" />
<img width="978" height="799" alt="image" src="https://github.com/user-attachments/assets/b5a80f33-dd33-40ef-9965-da2ff95a1c3a" />
<img width="896" height="808" alt="image" src="https://github.com/user-attachments/assets/1e55d63b-c528-4ca6-bbe8-fec322a54071" />
<img width="1053" height="825" alt="image" src="https://github.com/user-attachments/assets/ac735424-f4a5-46db-a850-ef5be0cd3d5c" />
<img width="1077" height="800" alt="image" src="https://github.com/user-attachments/assets/dbc4e10f-c492-4179-9c45-b47724822869" />
<img width="1074" height="808" alt="image" src="https://github.com/user-attachments/assets/921589d3-3a01-4b8b-b9ce-07d1a9f8a2d8" />
<img width="1126" height="825" alt="image" src="https://github.com/user-attachments/assets/700507a9-8503-47fd-b107-0f94ff30f1bf" />
<img width="1243" height="631" alt="image" src="https://github.com/user-attachments/assets/8b84238d-2b00-4ac5-81ce-c8ee0d065602" />

# Prompt Iteration 1

Give me five Machine Learning project ideas using Python.

### AI Response
<img width="1225" height="728" alt="image" src="https://github.com/user-attachments/assets/8c09b2b9-672e-4fec-bae8-a84d9dee7ca4" />
<img width="1364" height="785" alt="image" src="https://github.com/user-attachments/assets/3f2e471e-b4dd-4a7a-9fb0-d9de804d95ea" />
<img width="1172" height="534" alt="image" src="https://github.com/user-attachments/assets/430e882f-4b4c-43c5-bc89-485c563032c7" />

---

# Prompt Iteration 2

Give me five Machine Learning project ideas using Python that I can include in my GitHub portfolio for internship applications.

### AI Response
<img width="1283" height="780" alt="image" src="https://github.com/user-attachments/assets/0040c705-c17f-4fb9-866a-50f2a523f052" />
<img width="1141" height="793" alt="image" src="https://github.com/user-attachments/assets/ad2f4c1e-bb9c-4e8a-b68e-c3739e725e64" />
<img width="1319" height="760" alt="image" src="https://github.com/user-attachments/assets/0651d6cf-b6cd-4d64-9ed0-d3ca7e86ec23" />
<img width="1218" height="770" alt="image" src="https://github.com/user-attachments/assets/0808d57c-ff31-4911-a969-fa5494b239a0" />
<img width="1323" height="797" alt="image" src="https://github.com/user-attachments/assets/273ccc97-ffca-4c72-9e77-4fd4bb082a91" />
<img width="1340" height="791" alt="image" src="https://github.com/user-attachments/assets/d35a427c-6f1e-4daa-8f4c-a0e81a8341cc" />
<img width="1175" height="768" alt="image" src="https://github.com/user-attachments/assets/bb906dc6-a24f-41aa-8480-36b69249f6ad" />
<img width="1204" height="697" alt="image" src="https://github.com/user-attachments/assets/262c6784-5eb7-4b9c-807e-53cabd817888" />
<img width="1320" height="627" alt="image" src="https://github.com/user-attachments/assets/9228ccf3-85f7-4ff0-b6c7-2c39b8539853" />

# Conclusion

Day 6 demonstrated that reliable prompting depends on two important techniques:

- Grounding the model using only the provided information.
- Allowing the model to admit when information is unavailable instead of guessing.

Improving prompts one change at a time also made it easier to understand which modifications produced better results.
