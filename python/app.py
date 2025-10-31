from collections import Counter
import re

text = input("요약할 문장을 입력하세요: ")

words = re.findall(r'\w+', text.lower())
common = [w for w, _ in Counter(words).most_common(5)]

sentences = re.split(r'(?<=[.!?]) +', text)
summary = [s for s in sentences if any(w in s.lower() for w in common)]

print("\n📄 요약 결과:")
for s in summary[:3]:
    print("-", s.strip())
