print("Welcome to the AI Mood Checker!")
mood = input("How are you feeling today? ").lower()

if "happy" in mood:
    print("😊 I'm glad you're feeling good! Keep shining!")
elif "sad" in mood:
    print("💙 It's okay to feel sad sometimes. Take care of yourself.")
elif "tired" in mood:
    print("😴 Rest is important. Don't forget to take a break.")
elif "angry" in mood:
    print("😤 Try to take a deep breath. I'm here for you.")
else:
    print("🤖 Thanks for sharing. I'm always here to listen!")
