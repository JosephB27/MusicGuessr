# MusicGuessr - Project Context

## Project Overview

**MusicGuessr** is a Python-based music guessing game developed as a final Computer Programming course project (ICS4U1) by Joseph Bath, Vincenzo Milano, and Ethan Corno in June 2021. The game challenges players to identify song names by watching short video clips.

## Technology Stack

- **Primary Language**: Python
- **Game Framework**: Pygame
- **Video Processing**: 
  - `pyvidplayer` (custom video player implementation)
  - `ffpyplayer` (media player backend)
  - `pymediainfo` (media file analysis)

## Dependencies

```txt
pygame
pymediainfo
ffpyplayer
```

## Core Architecture

### File Structure
```
MusicGuessr/
├── MusicGuessr.py         # Main game file (510 lines)
├── pyvidplayer.py         # Custom video player class (86 lines)
├── button.py              # UI Button class (30 lines)
├── requirements.txt       # Dependencies
├── tempCodeRunnerFile.py  # Temporary file
├── Assets/
│   ├── Videos/            # 15 music video files (video1.mp4 - video15.mp4)
│   ├── bg.png             # Background image
│   ├── bgMusic.wav        # Background music
│   ├── Beep.wav           # Countdown sound
│   ├── Gong.wav           # Rules intro sound
│   ├── hoverSound.wav     # UI hover sound
│   ├── gameFont.ttf       # Primary game font
│   ├── fontShaded.ttf     # Title font
│   ├── Play Rect.png      # Play button graphic
│   ├── Options Rect.png   # Options button graphic
│   └── Quit Rect.png      # Quit button graphic
└── __pycache__/           # Python cache files
```

## Game Mechanics

### Core Game Flow
1. **Main Menu** → **Rules** → **Countdown** → **Video Display** → **Results** → **Leaderboard**
2. Game supports 1-4 players and 1-15 rounds (configurable in options)
3. Players guess song names by typing during video playback
4. Scoring based on correct/incorrect guesses

### Answer Key
The game includes 15 predefined songs:
- "Grenade", "Baby", "Beautiful Girls", "Broken", "Danza Kaduro"
- "Ego", "Just Cant Get Enough", "Love Me Again", "Papaoutai"
- "Pursuit of Happiness", "Riptide", "Rude", "Summer"
- "Sweater Weather", "Young Girls"

## Key Classes and Functions

### `Video` Class (`pyvidplayer.py`)
- Custom video player built on `ffpyplayer` and `pymediainfo`
- Handles video playback, seeking, pausing, and rendering
- Methods: `get_file_data()`, `restart()`, `close()`, `set_size()`, `update()`, `draw()`

### `Button` Class (`button.py`)
- UI component for interactive buttons
- Features hover effects and click detection
- Methods: `update()`, `checkForInput()`, `changeColor()`

### Main Game Functions (`MusicGuessr.py`)
- `main_menu()`: Entry point, navigation hub
- `options()`: Configure players (1-4) and rounds (1-15), audio mute toggle
- `rules()`: Display game instructions
- `countdown()`: 6-second countdown before each round
- `displayVideo()`: Core gameplay - video playback with text input
- `results()`: Show correct/incorrect feedback
- `leaderboard()`: Final score display
- `play()`: Orchestrates complete game flow

## Technical Details

### Display Configuration
- **Resolution**: 1450x750 pixels
- **Color Scheme**: Pink (`#EA4492`) and blue (`#041B2D`) theme
- **Fonts**: Custom TTF fonts for game and title text

### Audio System
- Background music with mute functionality
- Sound effects for UI interactions (beep, gong)
- Video audio playback through `ffpyplayer`

### Video Processing
- 15 pre-loaded MP4 files in `Assets/Videos/`
- Random video selection with basic duplicate prevention
- Video scaling to 900x550 pixels during playback

### User Input
- Text input field for song name guessing
- Case-insensitive matching
- No punctuation required in answers
- Enter key submission, backspace editing

## Known Issues & Limitations

1. **Video Selection Bug**: The duplicate prevention logic has a scope issue - `list` is recreated each function call
2. **File Path Handling**: Uses Windows-style backslashes (`\\`) which may cause cross-platform issues
3. **Asset Case Sensitivity**: Mixed case in asset loading (`assets/` vs `Assets/`)
4. **Memory Management**: No explicit video cleanup after playback
5. **Error Handling**: Limited error handling for missing assets or corrupted files

## Development Notes

### Code Style
- Mix of PascalCase and snake_case naming
- Global variables extensively used
- Inline comments for major sections
- Some unused variables (`clients`, `currentTime`, etc.)

### Pygame Integration
- Standard Pygame event loop pattern
- Manual display updates and clock management
- Custom font loading and rendering
- Rectangle-based collision detection for UI

## Deployment Considerations

1. **Asset Dependencies**: All media files must be present in `Assets/` directory
2. **Python Environment**: Requires Python with Pygame and media processing libraries
3. **Platform Compatibility**: Currently optimized for Windows (file paths, audio codecs)
4. **Performance**: Video decoding may require adequate CPU/GPU resources

## Future Enhancement Opportunities

1. **Cross-platform compatibility** (file path normalization)
2. **Better video selection algorithm** (prevent duplicates properly)
3. **Multiplayer scoring system** (currently tracks only single player)
4. **Dynamic song library** (JSON-based answer key)
5. **Error handling and logging**
6. **Configuration file** for settings persistence
7. **Audio visualization** during video playback
8. **Difficulty levels** (partial song names, hints)

## Running the Game

Execute `python MusicGuessr.py` from the project root directory. Ensure all dependencies are installed and the `Assets/` folder contains all required media files. 