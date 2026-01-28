# 🆘 Can't Find TripBud? Here's How to Locate It

## Step 1: Find Your Downloads Folder

The tripbud.zip file is probably in your Downloads folder. Let's navigate there:

```bash
cd ~/Downloads
```

## Step 2: List Files to Confirm

```bash
ls -la | grep tripbud
```

You should see `tripbud.zip`

## Step 3: Unzip the File

```bash
unzip tripbud.zip
```

This creates a `tripbud` folder in your Downloads.

## Step 4: Navigate Into TripBud

```bash
cd tripbud
ls
```

You should see:
- backend/
- frontend/
- README.md
- QUICKSTART.md
- etc.

## 🎯 Full Command Sequence (Copy & Paste This!)

```bash
# Go to Downloads
cd ~/Downloads

# Unzip (if you haven't already)
unzip tripbud.zip

# Enter the project
cd tripbud

# Verify you're in the right place
ls

# NOW you can follow the QUICKSTART.md instructions!
```

## Alternative: If Downloads Doesn't Work

Maybe you saved it somewhere else. Let's find it:

```bash
# Search your entire home directory for tripbud
find ~ -name "tripbud.zip" 2>/dev/null

# Or search for the folder
find ~ -type d -name "tripbud" 2>/dev/null
```

## 🚀 Once You Find It

Then run:

### Terminal 1 - Backend
```bash
cd /path/to/tripbud/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Terminal 2 - Frontend
```bash
cd /path/to/tripbud/frontend
npm install
npm run dev
```

## 📍 Still Stuck?

Tell me where you saved the tripbud.zip file and I'll give you the exact commands!
