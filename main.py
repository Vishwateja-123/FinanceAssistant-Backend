@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message', '')
    
    if 'spend' in user_message.lower():
        response = "You spent $450 last month on groceries and rent."
    elif 'save' in user_message.lower():
        response = "You saved $150 last month by cooking at home!"
    else:
        response = "I'm still learning! Can you rephrase your question?"

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run()
