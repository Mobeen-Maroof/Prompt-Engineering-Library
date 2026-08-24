def research(topic):
    data = {
        "Artificial Intelligence":
            {
                "Topic": "Artificial Intelligence",
                "Definition": "AI enables machines to perform tasks that normally require human intelligence.",
                "Applications": [
                    "Healthcare",
                    "Education",
                    "Finance",
                    "Robotics"
                ]
            },

        "Machine Learning":
            {
                "Topic": "Machine Learning",
                "Definition": "Machine Learning is a subset of Artificial Intelligence.",
                "Applications": [
                    "Recommendation Systems",
                    "Fraud Detection",
                    "Prediction"
                ]
            }
    }

    return data.get(topic, {"Error": "Topic not found"})