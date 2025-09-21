# Virtual Hand Gesture Keyboard

A computer vision-based virtual keyboard that allows users to type using hand gestures detected through a camera feed. The system uses MediaPipe hand tracking and OpenCV to create an interactive typing experience controlled entirely by hand movements.

## 🎥 Project Demo
[**Watch the Demo Video**](https://drive.google.com/file/d/1WXENJlqLEa_FohsthdufYV21LKudEPme/view?usp=sharing)

## 🌟 Features

- **Contactless Typing**: Type without touching any physical keyboard
- **Real-time Hand Tracking**: Uses advanced hand landmark detection
- **Visual Feedback**: Interactive button highlighting and click confirmation
- **Wireless Camera Support**: Works with IP camera feeds
- **QWERTY Layout**: Familiar keyboard layout for easy use
- **Backspace Functionality**: Delete characters using gesture control
- **Space Bar Support**: Add spaces between words

## 🔧 Technologies Used

### Core Libraries
- **OpenCV (cv2)**: Computer vision operations, video capture, and UI rendering
- **MediaPipe**: Advanced hand landmark detection and tracking
- **CVZone**: Simplified hand detection wrapper around MediaPipe
- **Pynput**: Keyboard control simulation (though not actively used in current implementation)
- **NumPy**: Numerical operations support

### Technical Approach

#### 1. Hand Tracking Algorithm
The system employs **MediaPipe Hand Landmark Detection** which:
- Detects up to 21 hand landmarks per hand
- Tracks fingertip positions in real-time
- Provides 3D coordinates for precise gesture recognition

#### 2. Distance-Based Click Detection
- **Pinch Gesture Recognition**: Measures distance between thumb tip (landmark 4) and index finger tip (landmark 8)
- **Click Threshold**: Distance < 25 pixels triggers a "click" event
- **Gesture Validation**: Ensures consistent detection before registering input

#### 3. Virtual Button System
- **Object-Oriented Design**: Custom `Button` class for each keyboard key
- **Collision Detection**: Checks if fingertip coordinates intersect with button boundaries
- **Visual Feedback System**: 
  - Default state: Black buttons with white text
  - Hover state: Blue highlighting when finger is over button
  - Click state: Green confirmation when gesture is detected

#### 4. Real-Time Video Processing Pipeline
```
Camera Feed → Hand Detection → Landmark Extraction → Gesture Recognition → UI Update → Text Output
```

## 🚀 Installation

### Prerequisites
```bash
pip install opencv-python
pip install cvzone
pip install mediapipe
pip install pynput
pip install numpy
```

### Setup
1. Clone or download the project files
2. Install required dependencies
3. Configure your camera URL in `main.py` (currently set to IP camera)
4. Run the application

## 💻 Usage

### Running the Application
```bash
python main.py
```

### How to Use
1. **Position Your Hand**: Hold your hand in front of the camera
2. **Navigate**: Move your index finger to hover over desired keys
3. **Type**: Bring thumb and index finger close together (pinch gesture) to "click"
4. **Visual Cues**:
   - Blue highlight = Key is selected
   - Green flash = Key has been pressed
   - Text appears in the display area at the top
5. **Special Functions**:
   - Use `<-` button for backspace
   - Use the space bar at the bottom for spaces

### Camera Configuration
The application is configured for an IP camera:
```python
url='http://192.168.10.2:8080/video'  # Modify this URL for your camera
```
For webcam use, change to:
```python
cap=cv2.VideoCapture(0)  # Use built-in webcam
```

## 🔬 Technical Implementation Details

### Hand Detection Parameters
- **Detection Confidence**: 0.8 (80% confidence threshold)
- **Maximum Hands**: 10 (supports multiple hands)
- **Tracking Landmarks**: 21 points per hand

### Button Layout Configuration
- **QWERTY Layout**: Standard 3-row keyboard arrangement
- **Button Size**: 80x80 pixels per key
- **Spacing**: 100 pixels between button centers
- **Positioning**: Dynamically calculated based on array indices

### Gesture Recognition Logic
```python
# Distance calculation between thumb tip and index finger tip
l, *, * = detector.findDistance(8, 4, img)

# Click detection threshold
if l < 25:
    # Register click event
    clickedText += button.text
```

### Performance Optimizations
- Efficient hand landmark processing
- Optimized button collision detection
- Minimal delay between gesture and response (0.2s sleep for debouncing)

## 🎯 Key Algorithms

### 1. Finger-Button Collision Detection
```python
if x < lmlist[8][0] < x+w and y < lmlist[8][1] < y+h:
    # Finger is over the button
```

### 2. Pinch Gesture Recognition
Uses Euclidean distance between specific hand landmarks to detect pinch gestures.

### 3. Text Management
- String concatenation for character input
- Slice operation for backspace functionality
- Real-time display updates

## 🔧 Configuration Options

### Camera Settings
- **Resolution**: 1280x720 (configurable)
- **Source**: IP camera or local webcam
- **Frame Rate**: Real-time processing

### Detection Sensitivity
- **Hand Detection**: 80% confidence threshold
- **Click Distance**: 25-pixel threshold (adjustable)
- **Debounce Time**: 200ms (prevents double-clicks)
