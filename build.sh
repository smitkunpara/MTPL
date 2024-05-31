echo "Building the project..."
python3.12 -m ensurepip --upgrade
python3.12 -m pip install -r requirements.txt
python3.12 manage.py collectstatic --noinput --clear
python3.12 manage.py migrate
echo "Project built successfully!"
