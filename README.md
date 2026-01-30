# ScreenGlow-ESP32

Простой Ambilight-подобный проект для ESP32 и RGB-ленты.  
Программа считывает средний цвет экрана ПК и передаёт его на ESP32 по Serial, создавая атмосферную подсветку.

## Возможности
- Работает с обычной RGB 5V лентой (не адресной)
- Автопоиск COM-порта
- Плавное сглаживание цветов
- Минимальная яркость (не уходит в 0)
- Усиление цветов для более выразительного эффекта
- Подходит для сборки в `.exe`

## Требования
- ESP32
- RGB-лента (3 канала)
- Python 3.9+
- Windows

---

# ScreenGlow-ESP32

A simple Ambilight-like project for ESP32 and RGB LED strips.  
The program reads the average screen color on a PC and sends it to the ESP32 via Serial, creating ambient backlighting.

## Features
- Works with basic 5V RGB LED strips (non-addressable)
- Automatic COM port detection
- Smooth color transitions
- Minimum brightness (never drops to 0)
- Color boost for more vivid visuals
- Ready to be packed into a `.exe`

## Requirements
- ESP32
- RGB LED strip (3-channel)
- Python 3.9+
- Windows
