# Video Signal Coding System and Method of Coding Video Signal for Network Transmission, Video Output Apparatus, and Signal Conversion Apparatus

## Abstract

A video signal coding system for network transmission includes a video output apparatus and a signal conversion apparatus. The video output apparatus includes a decoding unit decoding a video signal encoded by a coding method using a motion vector and a superimposing unit superimposing reference control information containing at least a motion vector on a blanking period of the video signal. The signal conversion apparatus includes a separating unit separating the reference control information from the blanking period, an encoding unit encoding the video signal by the coding method using the motion vector, and a motion vector converting unit converting the motion vector in the reference control information into a motion vector corresponding to the coding method in the encoding unit. The encoding is performed using the converted motion vector.

## Background 

Video transmission over networks for applications like video phone, conference, and security monitoring requires highly efficient real-time encoding. Motion vector based coding is commonly used, but detecting motion vectors during encoding is computationally expensive. 

In a video coding system formed by combining a video output apparatus and a signal conversion apparatus, efficiently performing motion vector based encoding in the signal conversion apparatus is challenging. Providing a large circuit for motion vector detection increases cost and power consumption. 

Prior approaches have limitations:
- Transferring an uncompressed video signal requires the signal conversion apparatus to detect motion vectors from scratch
- Transferring an encoded video signal requires the signal conversion apparatus to have a decoder matching the coding method of the video output apparatus

## Summary

Embodiments provide a video coding system where:
- The video output apparatus superimposes reference control info with motion vectors on the blanking period of the decoded/captured video signal 
- The signal conversion apparatus separates this reference control info, converts the motion vectors to match its own coding method, and uses them for efficient encoding
- This allows efficient motion vector coding without requiring expensive motion detection circuits or decoders matching the video output apparatus

## Detailed Description

Figure 3 shows an embodiment with:
- Video output apparatus 1 (e.g. camcorder)
- Signal conversion apparatus 8 (e.g. network TV)

The video output apparatus includes:  
- Imaging unit 2
- Encoding unit 3 (e.g. MPEG-2 encoder)
- Superimposing unit 4 
- Memory 5 
- Decoding unit 6 (e.g. MPEG-2 decoder)

The encoding unit 3 encodes live video and provides reference control info (motion vectors, macroblock type, picture type/size, frame rate) to the superimposing unit 4.

The decoding unit 6 decodes recorded video and provides reference control info to the superimposing unit 4.

The superimposing unit 4 superimposes the reference control info on the blanking period of the live/decoded video signal.

The signal conversion apparatus includes:
- Separating unit 9 
- Size/frame rate converting unit 10
- Motion vector converting unit 11
- Encoding unit 12 (e.g. H.261 encoder)

The separating unit 9 separates the reference control info from the input video signal's blanking period. 

The size/frame rate converting unit 10 adjusts the video to suit the network transmission.

The motion vector converting unit 11 converts the separated motion vectors to match the encoding unit 12's coding method.

The encoding unit 12 uses the converted motion vectors for efficient encoding without full motion search.

Various additional optimizations are discussed, such as compressing the reference control info, selectively transmitting motion vectors, bidirectional control signaling between apparatuses, different configurations for live vs recorded video, etc.
