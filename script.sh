./OTPgen.py 20000 key.bin
hexdump -C -n 256 key.bin
./OTPenc.py key.bin msg.png cipher.bin
hexdump -C -n 256 msg.png
hexdump -C -n 256 cipher.bin
./OTPdec.py key.bin cipher.bin dec.png
hexdump -C -n 256 dec.png
