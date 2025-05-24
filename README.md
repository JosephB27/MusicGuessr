**MusicGuessr** is a Python-based music guessing game developed as a final Computer Programming course project (ICS4U1) by Joseph Bath, Vincenzo Milano, and Ethan Corno in June 2021. The game challenges players to identify song names by watching short video clips.

## 🕹️ How to Play

1. **Main Menu:** Start the game, view rules, or configure options.
2. **Options:** Set number of players, rounds, and toggle audio.
3. **Gameplay:** Watch a video, type your guess, and submit.
4. **Results:** See if your guess was correct.
5. **Leaderboard:** View final scores.

## 🎵 Song List

- Grenade
- Baby
- Beautiful Girls
- Broken
- Danza Kaduro
- Ego
- Just Cant Get Enough
- Love Me Again
- Papaoutai
- Pursuit of Happiness
- Riptide
- Rude
- Summer
- Sweater Weather
- Young Girls

## ⚙️ Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/JosephB27/MusicGuessr.git
   cd MusicGuessr
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Ensure all assets are in the `Assets/` folder.**

## 🚀 Running the Game

```sh
python MusicGuessr.py
```

## 📝 Dependencies

- pygame
- pymediainfo
- ffpyplayer

## ⚠️ Known Issues

- Duplicate video prevention logic may not work as intended.
- File paths are Windows-style; may need adjustment for other OSes.
- Asset loading is case-sensitive.
- Limited error handling for missing/corrupt files.

## 💡 Future Enhancements

- Cross-platform compatibility
- Improved video selection algorithm
- Multiplayer scoring
- Dynamic song library (JSON-based)
- Better error handling and logging
- Config file for settings
- Audio visualization
- Difficulty levels

## 📄 License

This project was developed for educational purposes.

---

> **Developed by Joseph Bath, Vincenzo Milano, and Ethan Corno (June 2021)**
