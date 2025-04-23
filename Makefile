PYTHON := python
ENTRY := -m aiagent.cli

track:
	$(PYTHON) $(ENTRY) track $(repo)

list:
	$(PYTHON) $(ENTRY) list

remove:
	$(PYTHON) $(ENTRY) remove $(repo)

update:
	$(PYTHON) $(ENTRY) update

help:
	@echo "Usage:"
	@echo "  make track repo=owner/repo-name"
	@echo "  make list"
	@echo "  make remove repo=owner/repo-name"
	@echo "  make update"

