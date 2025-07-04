import openai

def run_valuation_agent(user_prompt):
    system_prompt = (
        "You are a valuation expert. Estimate the intrinsic value of a stock using DCF analysis, "
        "PE multiples, or other standard methods. Provide a clear rationale for your estimate. "
        "If the question is broad, make assumptions. Be analytical, structured, and transparent."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.6
    )

    return response.choices[0].message.content.strip()
