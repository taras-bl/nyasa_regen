echo "Step 0. Create folder structure."
mkdir ../$1
mkdir ../$1/input
mkdir ../$1/interim
mkdir ../$1/output
mkdir ../$1/postprocessed
mkdir ../$1/md
mkdir ../$1/orig
echo "Step 1. Preprocess input. Store in interim."
python preprocess.py $1
echo "Step 2. Convert to Devanagari. Store in output."
python converter.py $1
echo "Step 3. Postprocess the output. Store in postprocessed."
python postprocess.py $1
echo "Step 4. Correct known issues in conversion. Stored in postprocessed itself."
python issue1.py $1
echo "Step 5. Create .md files based on the postprocessed files. Store in md folder."
python create_md.py $1
