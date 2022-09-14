```
1. Run `get_all_tags_and_sessions.py` to generate JSON files of ALL sessions and ALL tag combinations (this only has to be done once).
2. Run UI.py to trigger the UI interface and then select which tags you want to filter by. Note that this is a boolean AND operation
currently, so will operate as follows: tag_1 AND tag_2 AND ... etc. Might need to change this to an OR operation...
3. Select which filtered sessions you want to output (Need to get them exported as CSVs but for now just a list of session_IDs is returned.)
4. A file named `output_session_IDs.txt` will be returned containing the session IDs you require.
```
