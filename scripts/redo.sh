echo "Step 1. Preprocess input. Store in interim."
python preprocess.py
echo "Step 2. Convert to Devanagari. Store in output."
python converter.py
echo "Step 3. Postprocess the output. Store in postprocessed."
python postprocess.py
echo "Step 4. Correct known issues in conversion. Stored in postprocessed itself."
python issue1.py
echo "Step 5. Create .md files based on the postprocessed files. Store in md folder."
python create_md.py
