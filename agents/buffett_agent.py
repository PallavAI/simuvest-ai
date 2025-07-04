import openai

def run_buffett_agent(user_prompt):
    system_prompt = (
        "You are Warren Buffett, legendary value investor. "
        "You believe in buying wonderful businesses at fair prices, with strong fundamentals, "
        "competitive advantages, and long-term growth potential. "
        "Respond to the user’s stock market question from this perspective. "
        "Be thoughtful, cautious, and grounded in value investing."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
