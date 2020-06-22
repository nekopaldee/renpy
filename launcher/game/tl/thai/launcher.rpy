# TODO: Translation updated at 2020-06-20 18:40

translate thai strings:

    # game/about.rpy:39
    old "[version!q]"
    new "เรน'ไพ [renpy.version_only]"

    # game/about.rpy:43
    old "View license"
    new "ดูสัญญา"

    # game/add_file.rpy:28
    old "FILENAME"
    new "ชื่อไฟล์"

    # game/add_file.rpy:28
    old "Enter the name of the script file to create."
    new "ใส่ชื่อไฟล์สคริปท์ที่ต้องการจะสร้าง"

    # game/add_file.rpy:37
    old "The file name may not be empty."
    new "ชื่อไฟล์ไม่สามารถเว้นว่างได้"

    # game/add_file.rpy:41
    old "The filename must have the .rpy extension."
    new "ชื่อไฟล์ต้องต่อท้ายด้วยนามสกุล .rpy"

    # game/add_file.rpy:50
    old "The file already exists."
    new "มีไฟล์นี้อยู่แล้ว"

    # game/add_file.rpy:61
    old "# Ren'Py automatically loads all script files ending with .rpy. To use this\n# file, define a label and jump to it from another file.\n"
    new "# เรน'ไพ จะโหลดไฟล์สคริปที่ลงท้ายด้วย .rpy ทั้งหมดโดยอัตโนมัติ\n# หากต้องการใช้ไฟล์นี้ กรุณากำหนดชื่อเรียก และเรียกใช้จากอีกไฟล์หนึ่ง\n"

    # game/android.rpy:30
    old "To build Android packages, please download RAPT, unzip it, and place it into the Ren'Py directory. Then restart the Ren'Py launcher."
    new "ในการสร้างไฟล์สำหรับ Android กรุณาดาวน์โหลด RAPT และแตกไฟล์ไว้ที่โฟลเดอร์ของเรน'ไพ หลังจากนั้นปิด และเปิดเรน'ไพอีกครั้งหนึ่ง"

    # game/android.rpy:31
    old "A 64-bit/x64 Java 8 Development Kit is required to build Android packages on Windows. The JDK is different from the JRE, so it's possible you have Java without having the JDK.\n\nPlease {a=http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html}download and install the JDK{/a}, then restart the Ren'Py launcher."
    new "จำเป็นต้องใช้ Java 8 Development Kit แบบ 64-bit/x64 ในการสร้างไฟล์สำหรับ Android บน Windows JDK นั้นแตกต่างจาก JRE ดังนั้นคุณอาจจะมี Java ที่ไม่มี JDK\n\nโปรด{a=http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html}ดาวน์โหลด และติดตั้ง JDK{/a} แล้วปิด และเปิดเรน'ไพใหม่อีกครั้งหนึ่ง"

    # game/android.rpy:32
    old "RAPT has been installed, but you'll need to install the Android SDK before you can build Android packages. Choose Install SDK to do this."
    new "RAPT ถูกติดตั้งแล้ว แต่คุณจำเป็นต้องติดตั้ง Android SDK ก่อนที่คุณจะสามารถสร้างไฟล์สำหรับ Android กรุณาเลือก ติดตั้ง SDK"

    # game/android.rpy:33
    old "RAPT has been installed, but a key hasn't been configured. Please create a new key, or restore android.keystore."
    new "RAPT ถูกติดตั้งแล้ว แต่กุญแจยังไม่ได้ถูกตั้งค่า กรุณาสร้างกุญแจใหม่ หรือกู้คืน android.keystore"

    # game/android.rpy:34
    old "The current project has not been configured. Use \"Configure\" to configure it before building."
    new "โปรเจกต์นี้ยังไม่ได้ถูกตั้งค่า กรุณาใช้ \"หน้าการตั้งค่า\" เพื่อตั้งค่าก่อนสร้างไฟล์"

    # game/android.rpy:35
    old "Choose \"Build\" to build the current project, or attach an Android device and choose \"Build & Install\" to build and install it on the device."
    new "เลือก \"สร้าง\" เพื่อสร้างไฟล์สำหรับโปรเจกต์นี้ หรือเชื่อมต่ออุปกรณ์ Android ของคุณ และเลือก \"สร้าง และติดตั้ง\" เพื่อสร้างไฟล์ และติดตั้งบนอุปกรณ์"

    # game/android.rpy:37
    old "Attempts to emulate an Android phone.\n\nTouch input is emulated through the mouse, but only when the button is held down. Escape is mapped to the menu button, and PageUp is mapped to the back button."
    new "กำลังจำลองเป็นมือถือ Android\n\nระบบสัมผัสสามารถควบคุมได้ด้วยการคลิกเมาส์เมาส์ ปุ่ม Escape จำลองเป็นปุ่มเมนู และปุ่ม PageUp จำลองเป็นปุ่มย้อนกลับ"

    # game/android.rpy:38
    old "Attempts to emulate an Android tablet.\n\nTouch input is emulated through the mouse, but only when the button is held down. Escape is mapped to the menu button, and PageUp is mapped to the back button."
    new "กำลังจำลองเป็นแท็บเล็ต Android\n\nระบบสัมผัสสามารถควบคุมได้ด้วยการคลิกเมาส์เมาส์ ปุ่ม Escape จำลองเป็นปุ่มเมนู และปุ่ม PageUp จำลองเป็นปุ่มย้อนกลับ"

    # game/android.rpy:39
    old "Attempts to emulate a televison-based Android console, like the OUYA or Fire TV.\n\nController input is mapped to the arrow keys, Enter is mapped to the select button, Escape is mapped to the menu button, and PageUp is mapped to the back button."
    new "กำลังจำลองเป็นโทรทัศน์ระบบ Android เหมือนกับ OUYA และ Fire TV\n\nโปรดใช้ปุ่มลูกศรในการควบคุมแทนรีโมต ปุ่ม Enter จำลองเป็นปุ่มเลือก ปุ่ม Escape จำลองเป็นปุ่มเมนู และปุ่ม PageUp จำลองเป็นปุ่มย้อนกลับ"

    # game/android.rpy:41
    old "Downloads and installs the Android SDK and supporting packages. Optionally, generates the keys required to sign the package."
    new "ดาวน์โหลด และติดตั้ง Android SDK พร้อมกับชุดไฟล์สนับสนุน หรือเลือกสร้างกุญแจที่จำเป็นสำหรับการสร้างไฟล์"

    # game/android.rpy:42
    old "Configures the package name, version, and other information about this project."
    new "ตั้งชื่อชุดไฟล์ เวอร์ชั่น และข้อมูลอื่น ๆ สำหรับโปรเจกต์นี้"

    # game/android.rpy:43
    old "Opens the file containing the Google Play keys in the editor.\n\nThis is only needed if the application is using an expansion APK. Read the documentation for more details."
    new "เปิดไฟล์ที่มีกุญแจของ Google Play ในตัวแก้ไข\n\nขั้นตอนนี้จำเป็นเฉพาะแอปพลิเคชันที่มีไฟล์ APK เพิ่มเติม โปรดอ่านคู่มือการใช้งานสำหรับข้อมูลเพิ่มเติม"

    # game/android.rpy:44
    old "Builds the Android package."
    new "สร้างชุดไฟล์สำหรับ Android"

    # game/android.rpy:45
    old "Builds the Android package, and installs it on an Android device connected to your computer."
    new "สร้างชุดไฟล์สำหรับ Android และติดตั้งลงบนอุปกรณ์ Android ที่เชื่อมต่ออยู่กับคอมพิวเตอร์"

    # game/android.rpy:46
    old "Builds the Android package, installs it on an Android device connected to your computer, then launches the app on your device."
    new "สร้างชุดไฟล์สำหรับ Android และติดตั้งลงบนอุปกรณ์ Android ที่เชื่อมต่ออยู่กับคอมพิวเตอร์ พร้อมกับเปิดแอปพลิเคชันบนอุปกรณ์"

    # game/android.rpy:48
    old "Retrieves the log from the Android device and writes it to a file."
    new "คัดลอกบันทึกการทำงานจากอุปกรณ์ Android และบันทึกเป็นไฟล์"

    # game/android.rpy:50
    old "Selects the Debug build, which can be accessed through Android Studio. Changing between debug and release builds requires an uninstall from your device."
    new "กรุณาเลือกชุดไฟล์สำหรับทดสอบที่สามารถเปิดได้ผ่าน Android Studio การสลับชุดไฟล์สำหรับทดสอบ และชุดไฟล์สำหรับเผยแพร่ จำเป็นต้องถอนการติดตั้งแอปพลิเคชันบนอุปกรณ์ของคุณ"

    # game/android.rpy:51
    old "Selects the Release build, which can be uploaded to stores. Changing between debug and release builds requires an uninstall from your device."
    new "กรุณาเลือกชุดไฟล์สำหรับการเผยแพร่ที่จะทำการอัปโหลดไปยังร้านค้า การสลับชุดไฟล์สำหรับทดสอบ และชุดไฟล์สำหรับเผยแพร่ จำเป็นต้องถอนการติดตั้งแอปพลิเคชันบนอุปกรณ์ของคุณ"

    # game/android.rpy:245
    old "Copying Android files to distributions directory."
    new "กำลังคัดลอกไฟล์ Android ไปยังโฟลเดอร์เผยแพร่"

    # game/android.rpy:313
    old "Android: [project.current.display_name!q]"
    new "Android: [project.current.display_name!q]"

    # game/android.rpy:333
    old "Emulation:"
    new "การจำลอง:"

    # game/android.rpy:342
    old "Phone"
    new "มือถือ"

    # game/android.rpy:346
    old "Tablet"
    new "แท็บเล็ต"

    # game/android.rpy:350
    old "Television"
    new "โทรทัศน์"

    # game/android.rpy:362
    old "Build:"
    new "ชุดไฟล์:"

    # game/android.rpy:377
    old "Release"
    new "สำหรับเผยแพร่"

    # game/android.rpy:384
    old "Install SDK & Create Keys"
    new "ติดตั้ง SDK และสร้างกุญแจ"

    # game/android.rpy:388
    old "Configure"
    new "ตั้งค่า"

    # game/android.rpy:392
    old "Build Package"
    new "สร้างชุดไฟล์"

    # game/android.rpy:396
    old "Build & Install"
    new "สร้างชุดไฟล์ และติดตั้ง"

    # game/android.rpy:400
    old "Build, Install & Launch"
    new "สร้างชุดไฟล์ ติดตั้ง และเปิด"

    # game/android.rpy:411
    old "Other:"
    new "อื่น ๆ :"

    # game/android.rpy:419
    old "Logcat"
    new "บันทึกการทำงาน"

    # game/android.rpy:452
    old "Before packaging Android apps, you'll need to download RAPT, the Ren'Py Android Packaging Tool. Would you like to download RAPT now?"
    new "ก่อนที่จะสร้างชุดไฟล์สำหรับ Android คุณจำเป็นต้องดาวน์โหลด RAPT (เครื่องมือสร้างชุดไฟล์ของเรน'ไพสำหรับ Android) คุณต้องการดาวน์โหลดเลยหรือไม่ ?"

    # game/android.rpy:505
    old "Retrieving logcat information from device."
    new "กำลังรับบันทึกการทำงานจากอุปกรณ์"

    # game/androidstrings.rpy:7
    old "{} is not a directory."
    new "{} ไม่ใช่ที่อยู่ที่ถูกต้อง"

    # game/androidstrings.rpy:8
    old "{} does not contain a Ren'Py game."
    new "{} ไม่มีไฟล์เกมของเรน'ไพ"

    # game/androidstrings.rpy:9
    old "Run configure before attempting to build the app."
    new "โปรดตั้งค่าก่อนสร้างชุดไฟล์"

    # game/androidstrings.rpy:10
    old "Google Play support is enabled, but build.google_play_key is not defined."
    new "ทำให้รองรับ Google Play แล้ว แต่ build.google_play_key ยังไม่ถูกกำหนด"

    # game/androidstrings.rpy:11
    old "Updating project."
    new "กำลังปรับปรุงโปรเจกต์"

    # game/androidstrings.rpy:12
    old "Creating assets directory."
    new "กำลังสร้างโฟลเดอร์ของไฟล์ที่จำเป็น"

    # game/androidstrings.rpy:13
    old "Creating expansion file."
    new "กำลังสร้างไฟล์เพิ่มเติม"

    # game/androidstrings.rpy:14
    old "Packaging internal data."
    new "กำลังสร้างชุดไฟล์"

    # game/androidstrings.rpy:15
    old "I'm using Gradle to build the package."
    new "ฉันกำลังใช้ Gradle เพื่อสร้างชุดไฟล์"

    # game/androidstrings.rpy:16
    old "Uploading expansion file."
    new "กำลังอัปโหลดไฟล์เพิ่มเติม"

    # game/androidstrings.rpy:17
    old "The build seems to have failed."
    new "การสร้างชุดไฟล์ล้มเหลว"

    # game/androidstrings.rpy:18
    old "Launching app."
    new "กำลังเปิดแอปพลิเคชัน"

    # game/androidstrings.rpy:19
    old "The build seems to have succeeded."
    new "การสร้างชุดไฟล์สำเร็จ"

    # game/androidstrings.rpy:20
    old "The arm64-v8a version works on newer Android devices, the armeabi-v7a version works on older devices, and the x86_64 version works on the simulator and chromebooks."
    new "แอปพลิเคชันฉบับ arm64-v8a สามารถใช้งานได้บนอุปกรณ์ Android รุ่นใหม่ ฉบับ armeabi-v7a สามารถใช้งานได้บนอุปกรณ์ที่เก่ากว่า และฉบับ x86_64 สามารถทำงานได้บนเครื่องจำลอง และโครมบุ๊ค"

    # game/androidstrings.rpy:21
    old "What is the full name of your application? This name will appear in the list of installed applications."
    new "แอปพลิเคชันของคุณมีชื่อว่าอะไร ? ชื่อนี้จะปรากฏบนรายชื่อแอปพลิเคชันที่ติดตั้งแล้วบนอุปกรณ์"

    # game/androidstrings.rpy:22
    old "What is the short name of your application? This name will be used in the launcher, and for application shortcuts."
    new "แอปพลิเคชันของคุณมีชื่อย่อว่าอะไร ? ชื่อนี้จะปรากฏอยู่บนหน้าจอหลัก และช็อตคัทของแอปพลิเคชัน"

    # game/androidstrings.rpy:23
    old "What is the name of the package?\n\nThis is usually of the form com.domain.program or com.domain.email.program. It may only contain ASCII letters and dots. It must contain at least one dot."
    new "ชุดไฟล์ของคุณมีชื่อว่าอะไร ?\n\nโดยปกติจะอยู่ในรูปแบบของ com.domain.program หรือ com.domain.email.program สามารถใช้ได้เฉพาะตัวอักษรในระบบ ASCII และจุดเท่านั้น โดยจำเป็นที่จะต้องมีจุดอย่างน้อยหนึ่งจุด"

    # game/androidstrings.rpy:24
    old "The package name may not be empty."
    new "ชุดของชุดไฟล์ไม่สามารถเว้นว่างได้"

    # game/androidstrings.rpy:25
    old "The package name may not contain spaces."
    new "ไม่สามารถใช้เว้นวรรคในชื่อของชุดไฟล์ได้"

    # game/androidstrings.rpy:26
    old "The package name must contain at least one dot."
    new "ชื่อของชุดไฟล์จำเป็นที่จะต้องมีจุดอย่างน้อยหนึ่งจุด"

    # game/androidstrings.rpy:27
    old "The package name may not contain two dots in a row, or begin or end with a dot."
    new "ชื่อของชุดไฟล์ไม่สามารถมีจุดสองจุดติดต่อกัน และไม่สามารถเริ่มต้นด้วยจุด หรือลงท้ายด้วยจุด"

    # game/androidstrings.rpy:28
    old "Each part of the package name must start with a letter, and contain only letters, numbers, and underscores."
    new "แต่ละช่วงของชุดไฟล์จำเป็นที่จะต้องเริ่มต้นด้วยตัวอักษร และสามารถมีได้เฉพาะตัวอักษร ตัวเลข และขีดล่าง"

    # game/androidstrings.rpy:29
    old "{} is a Java keyword, and can't be used as part of a package name."
    new "{} เป็นศัพท์สงวนของ Java ไม่สามารถใช้ตั้งชื่อชุดไฟล์ได้"

    # game/androidstrings.rpy:30
    old "What is the application's version?\n\nThis should be the human-readable version that you would present to a person. It must contain only numbers and dots."
    new "What is the application's version?\n\nThis should be the human-readable version that you would present to a person. It must contain only numbers and dots."

    # game/androidstrings.rpy:31
    old "The version number must contain only numbers and dots."
    new "The version number must contain only numbers and dots."

    # game/androidstrings.rpy:32
    old "What is the version code?\n\nThis must be a positive integer number, and the value should increase between versions."
    new "What is the version code?\n\nThis must be a positive integer number, and the value should increase between versions."

    # game/androidstrings.rpy:33
    old "The numeric version must contain only numbers."
    new "The numeric version must contain only numbers."

    # game/androidstrings.rpy:34
    old "How would you like your application to be displayed?"
    new "How would you like your application to be displayed?"

    # game/androidstrings.rpy:35
    old "In landscape orientation."
    new "In landscape orientation."

    # game/androidstrings.rpy:36
    old "In portrait orientation."
    new "In portrait orientation."

    # game/androidstrings.rpy:37
    old "In the user's preferred orientation."
    new "In the user's preferred orientation."

    # game/androidstrings.rpy:38
    old "Which app store would you like to support in-app purchasing through?"
    new "Which app store would you like to support in-app purchasing through?"

    # game/androidstrings.rpy:39
    old "Google Play."
    new "Google Play."

    # game/androidstrings.rpy:40
    old "Amazon App Store."
    new "Amazon App Store."

    # game/androidstrings.rpy:41
    old "Both, in one app."
    new "Both, in one app."

    # game/androidstrings.rpy:42
    old "Neither."
    new "Neither."

    # game/androidstrings.rpy:43
    old "Would you like to create an expansion APK?"
    new "Would you like to create an expansion APK?"

    # game/androidstrings.rpy:44
    old "No. Size limit of 100 MB on Google Play, but can be distributed through other stores and sideloaded."
    new "No. Size limit of 100 MB on Google Play, but can be distributed through other stores and sideloaded."

    # game/androidstrings.rpy:45
    old "Yes. 2 GB size limit, but won't work outside of Google Play. (Read the documentation to get this to work.)"
    new "Yes. 2 GB size limit, but won't work outside of Google Play. (Read the documentation to get this to work.)"

    # game/androidstrings.rpy:46
    old "Do you want to allow the app to access the Internet?"
    new "Do you want to allow the app to access the Internet?"

    # game/androidstrings.rpy:47
    old "Do you want to automatically update the generated project?"
    new "Do you want to automatically update the generated project?"

    # game/androidstrings.rpy:48
    old "Yes. This is the best choice for most projects."
    new "Yes. This is the best choice for most projects."

    # game/androidstrings.rpy:49
    old "No. This may require manual updates when Ren'Py or the project configuration changes."
    new "No. This may require manual updates when Ren'Py or the project configuration changes."

    # game/androidstrings.rpy:50
    old "Unknown configuration variable: {}"
    new "Unknown configuration variable: {}"

    # game/androidstrings.rpy:51
    old "I'm compiling a short test program, to see if you have a working JDK on your system."
    new "I'm compiling a short test program, to see if you have a working JDK on your system."

    # game/androidstrings.rpy:52
    old "I was unable to use javac to compile a test file. If you haven't installed the Java Development Kit yet, please download it from:\n\nhttp://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html\n\nThe JDK is different from the JRE, so it's possible you have Java without having the JDK. Without a working JDK, I can't continue."
    new "I was unable to use javac to compile a test file. If you haven't installed the Java Development Kit yet, please download it from:\n\nhttp://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html\n\nThe JDK is different from the JRE, so it's possible you have Java without having the JDK. Without a working JDK, I can't continue."

    # game/androidstrings.rpy:53
    old "The version of Java on your computer does not appear to be JDK 8, which is the only version supported by the Android SDK. If you need to install JDK 8, you can download it from:\n\nhttp://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html\n\nYou can also set the JAVA_HOME environment variable to use a different version of Java."
    new "The version of Java on your computer does not appear to be JDK 8, which is the only version supported by the Android SDK. If you need to install JDK 8, you can download it from:\n\nhttp://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html\n\nYou can also set the JAVA_HOME environment variable to use a different version of Java."

    # game/androidstrings.rpy:54
    old "The JDK is present and working. Good!"
    new "The JDK is present and working. Good!"

    # game/androidstrings.rpy:55
    old "The Android SDK has already been unpacked."
    new "The Android SDK has already been unpacked."

    # game/androidstrings.rpy:56
    old "Do you accept the Android SDK Terms and Conditions?"
    new "Do you accept the Android SDK Terms and Conditions?"

    # game/androidstrings.rpy:57
    old "I'm downloading the Android SDK. This might take a while."
    new "I'm downloading the Android SDK. This might take a while."

    # game/androidstrings.rpy:58
    old "I'm extracting the Android SDK."
    new "I'm extracting the Android SDK."

    # game/androidstrings.rpy:59
    old "I've finished unpacking the Android SDK."
    new "I've finished unpacking the Android SDK."

    # game/androidstrings.rpy:60
    old "I'm about to download and install the required Android packages. This might take a while."
    new "I'm about to download and install the required Android packages. This might take a while."

    # game/androidstrings.rpy:61
    old "I was unable to accept the Android licenses."
    new "I was unable to accept the Android licenses."

    # game/androidstrings.rpy:62
    old "I was unable to install the required Android packages."
    new "I was unable to install the required Android packages."

    # game/androidstrings.rpy:63
    old "I've finished installing the required Android packages."
    new "I've finished installing the required Android packages."

    # game/androidstrings.rpy:64
    old "You set the keystore yourself, so I'll assume it's how you want it."
    new "You set the keystore yourself, so I'll assume it's how you want it."

    # game/androidstrings.rpy:65
    old "You've already created an Android keystore, so I won't create a new one for you."
    new "You've already created an Android keystore, so I won't create a new one for you."

    # game/androidstrings.rpy:66
    old "I can create an application signing key for you. Signing an application with this key allows it to be placed in the Android Market and other app stores.\n\nDo you want to create a key?"
    new "I can create an application signing key for you. Signing an application with this key allows it to be placed in the Android Market and other app stores.\n\nDo you want to create a key?"

    # game/androidstrings.rpy:67
    old "I will create the key in the android.keystore file.\n\nYou need to back this file up. If you lose it, you will not be able to upgrade your application.\n\n\\You also need to keep the key safe. If evil people get this file, they could make fake versions of your application, and potentially steal your users' data.\n\nWill you make a backup of android.keystore, and keep it in a safe place?"
    new "I will create the key in the android.keystore file.\n\nYou need to back this file up. If you lose it, you will not be able to upgrade your application.\n\n\\You also need to keep the key safe. If evil people get this file, they could make fake versions of your application, and potentially steal your users' data.\n\nWill you make a backup of android.keystore, and keep it in a safe place?"

    # game/androidstrings.rpy:68
    old "Please enter your name or the name of your organization."
    new "Please enter your name or the name of your organization."

    # game/androidstrings.rpy:69
    old "Could not create android.keystore. Is keytool in your path?"
    new "Could not create android.keystore. Is keytool in your path?"

    # game/androidstrings.rpy:70
    old "I've finished creating android.keystore. Please back it up, and keep it in a safe place."
    new "I've finished creating android.keystore. Please back it up, and keep it in a safe place."

    # game/androidstrings.rpy:71
    old "It looks like you're ready to start packaging games."
    new "It looks like you're ready to start packaging games."

    # game/choose_directory.rpy:88
    old "Ren'Py was unable to run python with tkinter to choose the directory. Please install the python-tk or tkinter package."
    new "Ren'Py was unable to run python with tkinter to choose the directory. Please install the python-tk or tkinter package."

    # game/choose_directory.rpy:106
    old "The selected projects directory is not writable."
    new "The selected projects directory is not writable."

    # game/choose_theme.rpy:303
    old "Could not change the theme. Perhaps options.rpy was changed too much."
    new "Could not change the theme. Perhaps options.rpy was changed too much."

    # game/choose_theme.rpy:370
    old "Planetarium"
    new "Planetarium"

    # game/choose_theme.rpy:425
    old "Choose Theme"
    new "เลือกธีม"

    # game/choose_theme.rpy:438
    old "Theme"
    new "ธีม"

    # game/choose_theme.rpy:463
    old "Color Scheme"
    new "สี"

    # game/choose_theme.rpy:495
    old "Continue"
    new "ดำเนินการต่อ"

    # game/choose_theme.rpy:507
    old "changing the theme"
    new "กำลังเปลี่ยนธีม"

    # game/consolecommand.rpy:84
    old "INFORMATION"
    new "คำชี้แจง"

    # game/consolecommand.rpy:84
    old "The command is being run in a new operating system console window."
    new "The command is being run in a new operating system console window."

    # game/distribute.rpy:452
    old "Scanning project files..."
    new "Scanning project files..."

    # game/distribute.rpy:468
    old "Building distributions failed:\n\nThe build.directory_name variable may not include the space, colon, or semicolon characters."
    new "Building distributions failed:\n\nThe build.directory_name variable may not include the space, colon, or semicolon characters."

    # game/distribute.rpy:513
    old "No packages are selected, so there's nothing to do."
    new "No packages are selected, so there's nothing to do."

    # game/distribute.rpy:525
    old "Scanning Ren'Py files..."
    new "Scanning Ren'Py files..."

    # game/distribute.rpy:584
    old "All packages have been built.\n\nDue to the presence of permission information, unpacking and repacking the Linux and Macintosh distributions on Windows is not supported."
    new "All packages have been built.\n\nDue to the presence of permission information, unpacking and repacking the Linux and Macintosh distributions on Windows is not supported."

    # game/distribute.rpy:767
    old "Archiving files..."
    new "Archiving files..."

    # game/distribute.rpy:1092
    old "Unpacking the Macintosh application for signing..."
    new "Unpacking the Macintosh application for signing..."

    # game/distribute.rpy:1102
    old "Signing the Macintosh application...\n(This may take a long time.)"
    new "Signing the Macintosh application...\n(This may take a long time.)"

    # game/distribute.rpy:1125
    old "Creating the Macintosh DMG..."
    new "Creating the Macintosh DMG..."

    # game/distribute.rpy:1136
    old "Signing the Macintosh DMG..."
    new "Signing the Macintosh DMG..."

    # game/distribute.rpy:1331
    old "Writing the [variant] [format] package."
    new "Writing the [variant] [format] package."

    # game/distribute.rpy:1344
    old "Making the [variant] update zsync file."
    new "Making the [variant] update zsync file."

    # game/distribute.rpy:1454
    old "Processed {b}[complete]{/b} of {b}[total]{/b} files."
    new "Processed {b}[complete]{/b} of {b}[total]{/b} files."

    # game/distribute_gui.rpy:157
    old "Build Distributions: [project.current.display_name!q]"
    new "สร้างชุดไฟล์สำหรับการเล่นของ: [project.current.display_name!q]"

    # game/distribute_gui.rpy:171
    old "Directory Name:"
    new "ชื่อโฟลเดอร์:"

    # game/distribute_gui.rpy:175
    old "Executable Name:"
    new "ชื่อไฟล์สำหรับเปิดเล่น:"

    # game/distribute_gui.rpy:185
    old "Actions:"
    new "การกระทำ:"

    # game/distribute_gui.rpy:193
    old "Edit options.rpy"
    new "แก้ไข options.rpy"

    # game/distribute_gui.rpy:194
    old "Add from clauses to calls, once"
    new "Add from clauses to calls, once"

    # game/distribute_gui.rpy:195
    old "Refresh"
    new "โหลดใหม่"

    # game/distribute_gui.rpy:199
    old "Upload to itch.io"
    new "อัปโหลดไปยัง itch.io"

    # game/distribute_gui.rpy:215
    old "Build Packages:"
    new "สร้างชุดไฟล์สำหรับ:"

    # game/distribute_gui.rpy:234
    old "Options:"
    new "ตัวเลือกเพิ่มเติม:"

    # game/distribute_gui.rpy:239
    old "Build Updates"
    new "สร้างอัปเดท"

    # game/distribute_gui.rpy:241
    old "Add from clauses to calls"
    new "Add from clauses to calls"

    # game/distribute_gui.rpy:242
    old "Force Recompile"
    new "บังคับคอมไพล์ใหม่"

    # game/distribute_gui.rpy:246
    old "Build"
    new "สร้าง"

    # game/distribute_gui.rpy:250
    old "Adding from clauses to call statements that do not have them."
    new "Adding from clauses to call statements that do not have them."

    # game/distribute_gui.rpy:271
    old "Errors were detected when running the project. Please ensure the project runs without errors before building distributions."
    new "Errors were detected when running the project. Please ensure the project runs without errors before building distributions."

    # game/distribute_gui.rpy:288
    old "Your project does not contain build information. Would you like to add build information to the end of options.rpy?"
    new "Your project does not contain build information. Would you like to add build information to the end of options.rpy?"

    # game/dmgcheck.rpy:50
    old "Ren'Py is running from a read only folder. Some functionality will not work."
    new "Ren'Py is running from a read only folder. Some functionality will not work."

    # game/dmgcheck.rpy:50
    old "This is probably because Ren'Py is running directly from a Macintosh drive image. To fix this, quit this launcher, copy the entire %s folder somewhere else on your computer, and run Ren'Py again."
    new "This is probably because Ren'Py is running directly from a Macintosh drive image. To fix this, quit this launcher, copy the entire %s folder somewhere else on your computer, and run Ren'Py again."

    # game/editor.rpy:152
    old "(Recommended) A modern and approachable text editor."
    new "(Recommended) A modern and approachable text editor."

    # game/editor.rpy:164
    old "Up to 150 MB download required."
    new "Up to 150 MB download required."

    # game/editor.rpy:178
    old "A mature editor. Editra lacks the IME support required for Chinese, Japanese, and Korean text input."
    new "A mature editor. Editra lacks the IME support required for Chinese, Japanese, and Korean text input."

    # game/editor.rpy:179
    old "A mature editor. Editra lacks the IME support required for Chinese, Japanese, and Korean text input. On Linux, Editra requires wxPython."
    new "A mature editor. Editra lacks the IME support required for Chinese, Japanese, and Korean text input. On Linux, Editra requires wxPython."

    # game/editor.rpy:195
    old "This may have occured because wxPython is not installed on this system."
    new "This may have occured because wxPython is not installed on this system."

    # game/editor.rpy:197
    old "Up to 22 MB download required."
    new "Up to 22 MB download required."

    # game/editor.rpy:210
    old "A mature editor that requires Java."
    new "A mature editor that requires Java."

    # game/editor.rpy:210
    old "1.8 MB download required."
    new "1.8 MB download required."

    # game/editor.rpy:210
    old "This may have occured because Java is not installed on this system."
    new "This may have occured because Java is not installed on this system."

    # game/editor.rpy:219
    old "System Editor"
    new "System Editor"

    # game/editor.rpy:219
    old "Invokes the editor your operating system has associated with .rpy files."
    new "Invokes the editor your operating system has associated with .rpy files."

    # game/editor.rpy:235
    old "None"
    new "None"

    # game/editor.rpy:235
    old "Prevents Ren'Py from opening a text editor."
    new "Prevents Ren'Py from opening a text editor."

    # game/editor.rpy:338
    old "Edit [text]."
    new "Edit [text]."

    # game/editor.rpy:387
    old "An exception occured while launching the text editor:\n[exception!q]"
    new "An exception occured while launching the text editor:\n[exception!q]"

    # game/editor.rpy:519
    old "Select Editor"
    new "Select Editor"

    # game/editor.rpy:534
    old "A text editor is the program you'll use to edit Ren'Py script files. Here, you can select the editor Ren'Py will use. If not already present, the editor will be automatically downloaded and installed."
    new "A text editor is the program you'll use to edit Ren'Py script files. Here, you can select the editor Ren'Py will use. If not already present, the editor will be automatically downloaded and installed."

    # game/front_page.rpy:35
    old "Open [text] directory."
    new "Open [text] directory."

    # game/front_page.rpy:91
    old "PROJECTS:"
    new "โปรเจกต์:"

    # game/front_page.rpy:93
    old "refresh"
    new "โหลดใหม่"

    # game/front_page.rpy:120
    old "+ Create New Project"
    new "+ สร้างโปรเจกต์ใหม่"

    # game/front_page.rpy:130
    old "Launch Project"
    new "เปิดโปรเจกต์"

    # game/front_page.rpy:147
    old "[p.name!q] (template)"
    new "[p.name!q] (template)"

    # game/front_page.rpy:149
    old "Select project [text]."
    new "Select project [text]."

    # game/front_page.rpy:165
    old "Tutorial"
    new "Tutorial"

    # game/front_page.rpy:166
    old "The Question"
    new "The Question"

    # game/front_page.rpy:182
    old "Active Project"
    new "โปรเจกต์ที่เลือก"

    # game/front_page.rpy:190
    old "Open Directory"
    new "เปิดโฟลเดอร์"

    # game/front_page.rpy:195
    old "game"
    new "game"

    # game/front_page.rpy:196
    old "base"
    new "base"

    # game/front_page.rpy:197
    old "images"
    new "images"

    # game/front_page.rpy:198
    old "audio"
    new "audio"

    # game/front_page.rpy:199
    old "gui"
    new "gui"

    # game/front_page.rpy:204
    old "Edit File"
    new "แก้ไขไฟล์"

    # game/front_page.rpy:215
    old "Open project"
    new "เปิดไฟล์งาน"

    # game/front_page.rpy:217
    old "All script files"
    new "ไฟล์สคริปท์ทั้งหมด"

    # game/front_page.rpy:221
    old "Actions"
    new "การกระทำ"

    # game/front_page.rpy:230
    old "Navigate Script"
    new "ดูไฟล์สคริปท์"

    # game/front_page.rpy:231
    old "Check Script (Lint)"
    new "ตรวจสอบสคริปท์ (Lint)"

    # game/front_page.rpy:234
    old "Change/Update GUI"
    new "เปลี่ยน/ปรับปรุง GUI"

    # game/front_page.rpy:236
    old "Change Theme"
    new "เปลี่ยนธีม"

    # game/front_page.rpy:239
    old "Delete Persistent"
    new "ลบข้อมูลคงทน"

    # game/front_page.rpy:248
    old "Build Distributions"
    new "สร้างชุดไฟล์สำหรับเล่น"

    # game/front_page.rpy:250
    old "Android"
    new "Android"

    # game/front_page.rpy:251
    old "iOS"
    new "iOS"

    # game/front_page.rpy:252
    old "Web"
    new "เว็บไซต์"

    # game/front_page.rpy:252
    old "(Beta)"
    new "(ทดสอบ)"

    # game/front_page.rpy:253
    old "Generate Translations"
    new "สร้างชุดคำแปล"

    # game/front_page.rpy:254
    old "Extract Dialogue"
    new "แยกบทพูด"

    # game/front_page.rpy:271
    old "Checking script for potential problems..."
    new "กำลังตรวจสอบปัญห่ที่อาจเกิดขึ้นในสคริปท์..."

    # game/front_page.rpy:286
    old "Deleting persistent data..."
    new "กำลังลบข้อมูลคงทน..."

    # game/front_page.rpy:294
    old "Recompiling all rpy files into rpyc files..."
    new "กำลังคอมไพล์ไฟล์ rpy ให้เป็นไฟล์ rpyc อีกครั้ง..."

    # game/gui7.rpy:252
    old "Select Accent and Background Colors"
    new "Select Accent and Background Colors"

    # game/gui7.rpy:266
    old "Please click on the color scheme you wish to use, then click Continue. These colors can be changed and customized later."
    new "Please click on the color scheme you wish to use, then click Continue. These colors can be changed and customized later."

    # game/gui7.rpy:311
    old "{b}Warning{/b}\nContinuing will overwrite customized bar, button, save slot, scrollbar, and slider images.\n\nWhat would you like to do?"
    new "{b}Warning{/b}\nContinuing will overwrite customized bar, button, save slot, scrollbar, and slider images.\n\nWhat would you like to do?"

    # game/gui7.rpy:311
    old "Choose new colors, then regenerate image files."
    new "Choose new colors, then regenerate image files."

    # game/gui7.rpy:311
    old "Regenerate the image files using the colors in gui.rpy."
    new "Regenerate the image files using the colors in gui.rpy."

    # game/gui7.rpy:339
    old "What resolution should the project use? Although Ren'Py can scale the window up and down, this is the initial size of the window, the size at which assets should be drawn, and the size at which the assets will be at their sharpest.\n\nThe default of 1280x720 is a reasonable compromise."
    new "What resolution should the project use? Although Ren'Py can scale the window up and down, this is the initial size of the window, the size at which assets should be drawn, and the size at which the assets will be at their sharpest.\n\nThe default of 1280x720 is a reasonable compromise."

    # game/gui7.rpy:339
    old "Custom. The GUI is optimized for a 16:9 aspect ratio."
    new "Custom. The GUI is optimized for a 16:9 aspect ratio."

    # game/gui7.rpy:355
    old "WIDTH"
    new "WIDTH"

    # game/gui7.rpy:355
    old "Please enter the width of your game, in pixels."
    new "Please enter the width of your game, in pixels."

    # game/gui7.rpy:365
    old "The width must be a number."
    new "The width must be a number."

    # game/gui7.rpy:371
    old "HEIGHT"
    new "HEIGHT"

    # game/gui7.rpy:371
    old "Please enter the height of your game, in pixels."
    new "Please enter the height of your game, in pixels."

    # game/gui7.rpy:381
    old "The height must be a number."
    new "The height must be a number."

    # game/gui7.rpy:425
    old "Creating the new project..."
    new "Creating the new project..."

    # game/gui7.rpy:427
    old "Updating the project..."
    new "Updating the project..."

    # game/gui7.rpy:429
    old "creating a new project"
    new "creating a new project"

    # game/gui7.rpy:433
    old "activating the new project"
    new "activating the new project"

    # game/interface.rpy:119
    old "Documentation"
    new "คู่มือการใช้งาน"

    # game/interface.rpy:120
    old "Ren'Py Website"
    new "เว็บไซต์"

    # game/interface.rpy:121
    old "Ren'Py Games List"
    new "รายชื่อเกมที่ใช้ เรน'ไพ"

    # game/interface.rpy:129
    old "update"
    new "อัปเดท"

    # game/interface.rpy:131
    old "preferences"
    new "ตั้งค่า"

    # game/interface.rpy:132
    old "quit"
    new "ออก"

    # game/interface.rpy:136
    old "Ren'Py Sponsor Information"
    new "ข้อมูลผู้สนับสนุน เรน'ไพ"

    # game/interface.rpy:264
    old "Due to package format limitations, non-ASCII file and directory names are not allowed."
    new "Due to package format limitations, non-ASCII file and directory names are not allowed."

    # game/interface.rpy:360
    old "ERROR"
    new "ERROR"

    # game/interface.rpy:372
    old "opening the log file"
    new "opening the log file"

    # game/interface.rpy:394
    old "While [what!qt], an error occured:"
    new "While [what!qt], an error occured:"

    # game/interface.rpy:394
    old "[exception!q]"
    new "[exception!q]"

    # game/interface.rpy:427
    old "Text input may not contain the {{ or [[ characters."
    new "Text input may not contain the {{ or [[ characters."

    # game/interface.rpy:432
    old "File and directory names may not contain / or \\."
    new "File and directory names may not contain / or \\."

    # game/interface.rpy:438
    old "File and directory names must consist of ASCII characters."
    new "File and directory names must consist of ASCII characters."

    # game/interface.rpy:506
    old "PROCESSING"
    new "PROCESSING"

    # game/interface.rpy:523
    old "QUESTION"
    new "QUESTION"

    # game/interface.rpy:536
    old "CHOICE"
    new "CHOICE"

    # game/ios.rpy:28
    old "To build iOS packages, please download renios, unzip it, and place it into the Ren'Py directory. Then restart the Ren'Py launcher."
    new "To build iOS packages, please download renios, unzip it, and place it into the Ren'Py directory. Then restart the Ren'Py launcher."

    # game/ios.rpy:29
    old "The directory in where Xcode projects will be placed has not been selected. Choose 'Select Directory' to select it."
    new "The directory in where Xcode projects will be placed has not been selected. Choose 'Select Directory' to select it."

    # game/ios.rpy:30
    old "There is no Xcode project corresponding to the current Ren'Py project. Choose 'Create Xcode Project' to create one."
    new "There is no Xcode project corresponding to the current Ren'Py project. Choose 'Create Xcode Project' to create one."

    # game/ios.rpy:31
    old "An Xcode project exists. Choose 'Update Xcode Project' to update it with the latest game files, or use Xcode to build and install it."
    new "An Xcode project exists. Choose 'Update Xcode Project' to update it with the latest game files, or use Xcode to build and install it."

    # game/ios.rpy:33
    old "Attempts to emulate an iPhone.\n\nTouch input is emulated through the mouse, but only when the button is held down."
    new "Attempts to emulate an iPhone.\n\nTouch input is emulated through the mouse, but only when the button is held down."

    # game/ios.rpy:34
    old "Attempts to emulate an iPad.\n\nTouch input is emulated through the mouse, but only when the button is held down."
    new "Attempts to emulate an iPad.\n\nTouch input is emulated through the mouse, but only when the button is held down."

    # game/ios.rpy:36
    old "Selects the directory where Xcode projects will be placed."
    new "Selects the directory where Xcode projects will be placed."

    # game/ios.rpy:37
    old "Creates an Xcode project corresponding to the current Ren'Py project."
    new "Creates an Xcode project corresponding to the current Ren'Py project."

    # game/ios.rpy:38
    old "Updates the Xcode project with the latest game files. This must be done each time the Ren'Py project changes."
    new "Updates the Xcode project with the latest game files. This must be done each time the Ren'Py project changes."

    # game/ios.rpy:39
    old "Opens the Xcode project in Xcode."
    new "Opens the Xcode project in Xcode."

    # game/ios.rpy:41
    old "Opens the directory containing Xcode projects."
    new "Opens the directory containing Xcode projects."

    # game/ios.rpy:131
    old "The Xcode project already exists. Would you like to rename the old project, and replace it with a new one?"
    new "The Xcode project already exists. Would you like to rename the old project, and replace it with a new one?"

    # game/ios.rpy:225
    old "iOS: [project.current.display_name!q]"
    new "iOS: [project.current.display_name!q]"

    # game/ios.rpy:254
    old "iPhone"
    new "iPhone"

    # game/ios.rpy:258
    old "iPad"
    new "iPad"

    # game/ios.rpy:278
    old "Select Xcode Projects Directory"
    new "Select Xcode Projects Directory"

    # game/ios.rpy:282
    old "Create Xcode Project"
    new "Create Xcode Project"

    # game/ios.rpy:286
    old "Update Xcode Project"
    new "Update Xcode Project"

    # game/ios.rpy:291
    old "Launch Xcode"
    new "Launch Xcode"

    # game/ios.rpy:326
    old "Open Xcode Projects Directory"
    new "Open Xcode Projects Directory"

    # game/ios.rpy:359
    old "Before packaging iOS apps, you'll need to download renios, Ren'Py's iOS support. Would you like to download renios now?"
    new "Before packaging iOS apps, you'll need to download renios, Ren'Py's iOS support. Would you like to download renios now?"

    # game/ios.rpy:368
    old "XCODE PROJECTS DIRECTORY"
    new "XCODE PROJECTS DIRECTORY"

    # game/ios.rpy:368
    old "Please choose the Xcode Projects Directory using the directory chooser.\n{b}The directory chooser may have opened behind this window.{/b}"
    new "Please choose the Xcode Projects Directory using the directory chooser.\n{b}The directory chooser may have opened behind this window.{/b}"

    # game/ios.rpy:373
    old "Ren'Py has set the Xcode Projects Directory to:"
    new "Ren'Py has set the Xcode Projects Directory to:"

    # game/itch.rpy:43
    old "Downloading the itch.io butler."
    new "Downloading the itch.io butler."

    # game/itch.rpy:96
    old "The built distributions could not be found. Please choose 'Build' and try again."
    new "The built distributions could not be found. Please choose 'Build' and try again."

    # game/itch.rpy:134
    old "No uploadable files were found. Please choose 'Build' and try again."
    new "No uploadable files were found. Please choose 'Build' and try again."

    # game/itch.rpy:140
    old "The butler program was not found."
    new "The butler program was not found."

    # game/itch.rpy:140
    old "Please install the itch.io app, which includes butler, and try again."
    new "Please install the itch.io app, which includes butler, and try again."

    # game/itch.rpy:149
    old "The name of the itch project has not been set."
    new "The name of the itch project has not been set."

    # game/itch.rpy:149
    old "Please {a=https://itch.io/game/new}create your project{/a}, then add a line like \n{vspace=5}define build.itch_project = \"user-name/game-name\"\n{vspace=5} to options.rpy."
    new "Please {a=https://itch.io/game/new}create your project{/a}, then add a line like \n{vspace=5}define build.itch_project = \"user-name/game-name\"\n{vspace=5} to options.rpy."

    # game/mobilebuild.rpy:110
    old "{a=%s}%s{/a}"
    new "{a=%s}%s{/a}"

    # game/navigation.rpy:168
    old "Navigate: [project.current.display_name!q]"
    new "Navigate: [project.current.display_name!q]"

    # game/navigation.rpy:178
    old "Order: "
    new "Order: "

    # game/navigation.rpy:179
    old "alphabetical"
    new "alphabetical"

    # game/navigation.rpy:181
    old "by-file"
    new "by-file"

    # game/navigation.rpy:183
    old "natural"
    new "natural"

    # game/navigation.rpy:195
    old "Category:"
    new "Category:"

    # game/navigation.rpy:198
    old "files"
    new "files"

    # game/navigation.rpy:199
    old "labels"
    new "labels"

    # game/navigation.rpy:200
    old "defines"
    new "defines"

    # game/navigation.rpy:201
    old "transforms"
    new "transforms"

    # game/navigation.rpy:202
    old "screens"
    new "screens"

    # game/navigation.rpy:203
    old "callables"
    new "callables"

    # game/navigation.rpy:204
    old "TODOs"
    new "TODOs"

    # game/navigation.rpy:243
    old "+ Add script file"
    new "+ Add script file"

    # game/navigation.rpy:251
    old "No TODO comments found.\n\nTo create one, include \"# TODO\" in your script."
    new "No TODO comments found.\n\nTo create one, include \"# TODO\" in your script."

    # game/navigation.rpy:258
    old "The list of names is empty."
    new "The list of names is empty."

    # game/new_project.rpy:38
    old "New GUI Interface"
    new "New GUI Interface"

    # game/new_project.rpy:48
    old "Both interfaces have been translated to your language."
    new "Both interfaces have been translated to your language."

    # game/new_project.rpy:50
    old "Only the new GUI has been translated to your language."
    new "Only the new GUI has been translated to your language."

    # game/new_project.rpy:52
    old "Only the legacy theme interface has been translated to your language."
    new "Only the legacy theme interface has been translated to your language."

    # game/new_project.rpy:54
    old "Neither interface has been translated to your language."
    new "Neither interface has been translated to your language."

    # game/new_project.rpy:63
    old "The projects directory could not be set. Giving up."
    new "The projects directory could not be set. Giving up."

    # game/new_project.rpy:70
    old "Which interface would you like to use? The new GUI has a modern look, supports wide screens and mobile devices, and is easier to customize. Legacy themes might be necessary to work with older example code.\n\n[language_support!t]\n\nIf in doubt, choose the new GUI, then click Continue on the bottom-right."
    new "Which interface would you like to use? The new GUI has a modern look, supports wide screens and mobile devices, and is easier to customize. Legacy themes might be necessary to work with older example code.\n\n[language_support!t]\n\nIf in doubt, choose the new GUI, then click Continue on the bottom-right."

    # game/new_project.rpy:70
    old "Legacy Theme Interface"
    new "Legacy Theme Interface"

    # game/new_project.rpy:81
    old "You will be creating an [new_project_language]{#this substitution may be localized} language project. Change the launcher language in preferences to create a project in another language."
    new "โปรเจกต์ที่คุณกำลังสร้างจะเป็นโปรเจกต์ภาษาไทย หากคุณต้องการสร้างโปรเจกต์ภาษาอื่น กรุณาเปลี่ยนภาษาในหน้าตั้งค่าของโปรแกรม"

    # game/new_project.rpy:86
    old "PROJECT NAME"
    new "ชื่อโปรเจกต์"

    # game/new_project.rpy:86
    old "Please enter the name of your project:"
    new "กรุณาตั้งชื่อโปรเจกต์ของคุณ:"

    # game/new_project.rpy:96
    old "The project name may not be empty."
    new "ชื่อโปรเจกต์ไม่สามารถเว้นว่างได้"

    # game/new_project.rpy:102
    old "[project_name!q] already exists. Please choose a different project name."
    new "[project_name!q] already exists. Please choose a different project name."

    # game/new_project.rpy:106
    old "[project_dir!q] already exists. Please choose a different project name."
    new "[project_dir!q] already exists. Please choose a different project name."

    # game/new_project.rpy:124
    old "Choose Project Template"
    new "Choose Project Template"

    # game/new_project.rpy:142
    old "Please select a template to use for your new project. The template sets the default font and the user interface language. If your language is not supported, choose 'english'."
    new "Please select a template to use for your new project. The template sets the default font and the user interface language. If your language is not supported, choose 'english'."

    # game/preferences.rpy:73
    old "Launcher Preferences"
    new "ตั้งค่า"

    # game/preferences.rpy:94
    old "Projects Directory:"
    new "โฟลเดอร์โปรเจกต์:"

    # game/preferences.rpy:101
    old "[persistent.projects_directory!q]"
    new "[persistent.projects_directory!q]"

    # game/preferences.rpy:103
    old "Projects directory: [text]"
    new "Projects directory: [text]"

    # game/preferences.rpy:105
    old "Not Set"
    new "ไม่ได้ตั้ง"

    # game/preferences.rpy:120
    old "Text Editor:"
    new "เครืองมือแก้ไข:"

    # game/preferences.rpy:126
    old "Text editor: [text]"
    new "เครืองมือแก้ไข: [text]"

    # game/preferences.rpy:145
    old "Navigation Options:"
    new "ตัวเลือกการแสดงผล:"

    # game/preferences.rpy:149
    old "Include private names"
    new "แสดงชื่อเฉพาะ"

    # game/preferences.rpy:150
    old "Include library names"
    new "แสดงชื่อไลบารี่"

    # game/preferences.rpy:160
    old "Launcher Options:"
    new "ตัวเลือก Launcher:"

    # game/preferences.rpy:164
    old "Hardware rendering"
    new "แสดงผลด้วยฮาร์ดแวร์"

    # game/preferences.rpy:165
    old "Show edit file section"
    new "แสดงหมวดหมู่การแก้ไขไฟล์"

    # game/preferences.rpy:166
    old "Large fonts"
    new "แบบอักษรขนาดใหญ่"

    # game/preferences.rpy:169
    old "Console output"
    new "แสดงผลผ่านคอนโซล"

    # game/preferences.rpy:173
    old "Force new tutorial"
    new "บังคับสร้าง tutorial ใหม่"

    # game/preferences.rpy:177
    old "Legacy options"
    new "ตัวเลือกเก่า"

    # game/preferences.rpy:180
    old "Show templates"
    new "แสดงโปรเจกต์ต้นแบบ"

    # game/preferences.rpy:182
    old "Sponsor message"
    new "ข้อความผู้สนับสนุน"

    # game/preferences.rpy:202
    old "Open launcher project"
    new "เปิดโปรเจกต์ของ launcher"

    # game/preferences.rpy:216
    old "Language:"
    new "ภาษา:"

    # game/project.rpy:49
    old "After making changes to the script, press shift+R to reload your game."
    new "After making changes to the script, press shift+R to reload your game."

    # game/project.rpy:49
    old "Press shift+O (the letter) to access the console."
    new "Press shift+O (the letter) to access the console."

    # game/project.rpy:49
    old "Press shift+D to access the developer menu."
    new "Press shift+D to access the developer menu."

    # game/project.rpy:49
    old "Have you backed up your projects recently?"
    new "Have you backed up your projects recently?"

    # game/project.rpy:281
    old "Launching the project failed."
    new "Launching the project failed."

    # game/project.rpy:281
    old "Please ensure that your project launches normally before running this command."
    new "Please ensure that your project launches normally before running this command."

    # game/project.rpy:297
    old "Ren'Py is scanning the project..."
    new "Ren'Py is scanning the project..."

    # game/project.rpy:729
    old "Launching"
    new "Launching"

    # game/project.rpy:763
    old "PROJECTS DIRECTORY"
    new "PROJECTS DIRECTORY"

    # game/project.rpy:763
    old "Please choose the projects directory using the directory chooser.\n{b}The directory chooser may have opened behind this window.{/b}"
    new "Please choose the projects directory using the directory chooser.\n{b}The directory chooser may have opened behind this window.{/b}"

    # game/project.rpy:763
    old "This launcher will scan for projects in this directory, will create new projects in this directory, and will place built projects into this directory."
    new "This launcher will scan for projects in this directory, will create new projects in this directory, and will place built projects into this directory."

    # game/project.rpy:768
    old "Ren'Py has set the projects directory to:"
    new "Ren'Py has set the projects directory to:"

    # game/translations.rpy:91
    old "Translations: [project.current.display_name!q]"
    new "Translations: [project.current.display_name!q]"

    # game/translations.rpy:132
    old "The language to work with. This should only contain lower-case ASCII characters and underscores."
    new "The language to work with. This should only contain lower-case ASCII characters and underscores."

    # game/translations.rpy:158
    old "Generate empty strings for translations"
    new "Generate empty strings for translations"

    # game/translations.rpy:176
    old "Generates or updates translation files. The files will be placed in game/tl/[persistent.translate_language!q]."
    new "Generates or updates translation files. The files will be placed in game/tl/[persistent.translate_language!q]."

    # game/translations.rpy:196
    old "Extract String Translations"
    new "Extract String Translations"

    # game/translations.rpy:198
    old "Merge String Translations"
    new "Merge String Translations"

    # game/translations.rpy:203
    old "Replace existing translations"
    new "Replace existing translations"

    # game/translations.rpy:204
    old "Reverse languages"
    new "Reverse languages"

    # game/translations.rpy:208
    old "Update Default Interface Translations"
    new "Update Default Interface Translations"

    # game/translations.rpy:228
    old "The extract command allows you to extract string translations from an existing project into a temporary file.\n\nThe merge command merges extracted translations into another project."
    new "The extract command allows you to extract string translations from an existing project into a temporary file.\n\nThe merge command merges extracted translations into another project."

    # game/translations.rpy:252
    old "Ren'Py is generating translations...."
    new "Ren'Py is generating translations...."

    # game/translations.rpy:263
    old "Ren'Py has finished generating [language] translations."
    new "Ren'Py has finished generating [language] translations."

    # game/translations.rpy:276
    old "Ren'Py is extracting string translations..."
    new "Ren'Py is extracting string translations..."

    # game/translations.rpy:279
    old "Ren'Py has finished extracting [language] string translations."
    new "Ren'Py has finished extracting [language] string translations."

    # game/translations.rpy:299
    old "Ren'Py is merging string translations..."
    new "Ren'Py is merging string translations..."

    # game/translations.rpy:302
    old "Ren'Py has finished merging [language] string translations."
    new "Ren'Py has finished merging [language] string translations."

    # game/translations.rpy:313
    old "Updating default interface translations..."
    new "Updating default interface translations..."

    # game/translations.rpy:342
    old "Extract Dialogue: [project.current.display_name!q]"
    new "Extract Dialogue: [project.current.display_name!q]"

    # game/translations.rpy:358
    old "Format:"
    new "Format:"

    # game/translations.rpy:366
    old "Tab-delimited Spreadsheet (dialogue.tab)"
    new "Tab-delimited Spreadsheet (dialogue.tab)"

    # game/translations.rpy:367
    old "Dialogue Text Only (dialogue.txt)"
    new "Dialogue Text Only (dialogue.txt)"

    # game/translations.rpy:380
    old "Strip text tags from the dialogue."
    new "Strip text tags from the dialogue."

    # game/translations.rpy:381
    old "Escape quotes and other special characters."
    new "Escape quotes and other special characters."

    # game/translations.rpy:382
    old "Extract all translatable strings, not just dialogue."
    new "Extract all translatable strings, not just dialogue."

    # game/translations.rpy:410
    old "Ren'Py is extracting dialogue...."
    new "Ren'Py is extracting dialogue...."

    # game/translations.rpy:414
    old "Ren'Py has finished extracting dialogue. The extracted dialogue can be found in dialogue.[persistent.dialogue_format] in the base directory."
    new "Ren'Py has finished extracting dialogue. The extracted dialogue can be found in dialogue.[persistent.dialogue_format] in the base directory."

    # game/updater.rpy:63
    old "{b}Recommended.{/b} The version of Ren'Py that should be used in all newly-released games."
    new "{b}Recommended.{/b} The version of Ren'Py that should be used in all newly-released games."

    # game/updater.rpy:65
    old "Prerelease"
    new "Prerelease"

    # game/updater.rpy:66
    old "A preview of the next version of Ren'Py that can be used for testing and taking advantage of new features, but not for final releases of games."
    new "A preview of the next version of Ren'Py that can be used for testing and taking advantage of new features, but not for final releases of games."

    # game/updater.rpy:68
    old "Experimental"
    new "Experimental"

    # game/updater.rpy:69
    old "Experimental versions of Ren'Py. You shouldn't select this channel unless asked by a Ren'Py developer."
    new "Experimental versions of Ren'Py. You shouldn't select this channel unless asked by a Ren'Py developer."

    # game/updater.rpy:71
    old "Nightly"
    new "Nightly"

    # game/updater.rpy:72
    old "The bleeding edge of Ren'Py development. This may have the latest features, or might not run at all."
    new "The bleeding edge of Ren'Py development. This may have the latest features, or might not run at all."

    # game/updater.rpy:90
    old "Select Update Channel"
    new "Select Update Channel"

    # game/updater.rpy:101
    old "The update channel controls the version of Ren'Py the updater will download."
    new "The update channel controls the version of Ren'Py the updater will download."

    # game/updater.rpy:110
    old "• This version is installed and up-to-date."
    new "• This version is installed and up-to-date."

    # game/updater.rpy:118
    old "%B %d, %Y"
    new "%B %d, %Y"

    # game/updater.rpy:140
    old "An error has occured:"
    new "An error has occured:"

    # game/updater.rpy:142
    old "Checking for updates."
    new "Checking for updates."

    # game/updater.rpy:144
    old "Ren'Py is up to date."
    new "Ren'Py is up to date."

    # game/updater.rpy:146
    old "[u.version] is now available. Do you want to install it?"
    new "[u.version] is now available. Do you want to install it?"

    # game/updater.rpy:148
    old "Preparing to download the update."
    new "Preparing to download the update."

    # game/updater.rpy:150
    old "Downloading the update."
    new "Downloading the update."

    # game/updater.rpy:152
    old "Unpacking the update."
    new "Unpacking the update."

    # game/updater.rpy:154
    old "Finishing up."
    new "Finishing up."

    # game/updater.rpy:156
    old "The update has been installed. Ren'Py will restart."
    new "The update has been installed. Ren'Py will restart."

    # game/updater.rpy:158
    old "The update has been installed."
    new "The update has been installed."

    # game/updater.rpy:160
    old "The update was cancelled."
    new "The update was cancelled."

    # game/updater.rpy:177
    old "Ren'Py Update"
    new "Ren'Py Update"

    # game/updater.rpy:183
    old "Proceed"
    new "Proceed"

    # game/updater.rpy:188
    old "Fetching the list of update channels"
    new "Fetching the list of update channels"

    # game/updater.rpy:194
    old "downloading the list of update channels"
    new "downloading the list of update channels"

    # game/updater.rpy:198
    old "parsing the list of update channels"
    new "parsing the list of update channels"

    # game/web.rpy:119
    old "Web: [project.current.display_name!q]"
    new "Web: [project.current.display_name!q]"

    # game/web.rpy:149
    old "Build Web Application"
    new "Build Web Application"

    # game/web.rpy:150
    old "Build and Open in Browser"
    new "Build and Open in Browser"

    # game/web.rpy:151
    old "Open in Browser"
    new "Open in Browser"

    # game/web.rpy:152
    old "Open build directory"
    new "Open build directory"

    # game/web.rpy:156
    old "Support:"
    new "Support:"

    # game/web.rpy:164
    old "RenPyWeb Home"
    new "RenPyWeb Home"

    # game/web.rpy:165
    old "Beuc's Patreon"
    new "Beuc's Patreon"

    # game/web.rpy:183
    old "Ren'Py web applications require the entire game to be downloaded to the player's computer before it can start."
    new "Ren'Py web applications require the entire game to be downloaded to the player's computer before it can start."

    # game/web.rpy:187
    old "Current limitations in the web platform mean that loading large images, audio files, or movies may cause audio or framerate glitches, and lower performance in general."
    new "Current limitations in the web platform mean that loading large images, audio files, or movies may cause audio or framerate glitches, and lower performance in general."

    # game/web.rpy:196
    old "Before packaging web apps, you'll need to download RenPyWeb, Ren'Py's web support. Would you like to download RenPyWeb now?"
    new "Before packaging web apps, you'll need to download RenPyWeb, Ren'Py's web support. Would you like to download RenPyWeb now?"

