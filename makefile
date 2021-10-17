COURSE = cse107
GROUP_NAME = donovan_griego
ASSIGNMENT = lab8
TARGETS = nested.py cesaro.py design palindrome.py README.md
zip: $(TARGETS)
	zip $(COURSE)_$(GROUP_NAME)_$(ASSIGNMENT).zip $(TARGETS)