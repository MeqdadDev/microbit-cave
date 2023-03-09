# dht11.py - a microbit implementation of dht11
# author - Phil Hall, copyright (c)
#
# License - MIT

import microbit as uBit

DEGREES = u'\xb0'


class DataError(Exception):
    pass


class DHT11:
    def __init__(self, pin):
        self._pin = pin

    def read(self):
        # creating these locals speeds things up len() is very slow
        pin = self._pin
        pin2bit = self._pin2bit()
        buffer_ = bytearray(256)
        length = (len(buffer_) // 4) * 4

        for i in range(length, len(buffer_)):
            buffer_[i] = 1

        pin.write_digital(1)
        uBit.sleep(50)
        self._block_irq()

        pin.write_digital(0)
        uBit.sleep(20)

        pin.read_digital()
        pin.set_pull(pin.PULL_UP)

        if self._grab_bits(pin2bit, buffer_, length) != length:
            self._unblock_irq()
            raise Exception("Grab bits failed.")
        else:
            self._unblock_irq()

        # for b in buffer_:
        #    print(b, end = "")
        # print('')

        data = self._parse_data(buffer_)

        del buffer_

        if data is None or len(data) != 40:
            if data is None:
                bits = 0
            else:
                bits = len(data)
            raise DataError("Too many or too few bits " + str(bits))

        data = self._calc_bytes(data)

        checksum = self._calc_checksum(data)
        if data[4] != checksum:
            raise DataError("Checksum invalid.")

        temp = data[2] + (data[3] / 10)
        humid = data[0] + (data[1] / 10)
        return (temp, humid)

    def _pin2bit(self):
        # this is a dictionary, microbit.pinX can't be a __hash__
        pin = self._pin
        if pin == uBit.pin0:
            shift = 2
        elif pin == uBit.pin1:
            shift = 3
        elif pin == uBit.pin2:
            shift = 4
        elif pin == uBit.pin3:
            shift = 15
        elif pin == uBit.pin4:
            shift = 19
        elif pin == uBit.pin6:
            shift = 21
        elif pin == uBit.pin7:
            shift = 22
        elif pin == uBit.pin8:
            shift = 10
        elif pin == uBit.pin9:
            shift = 9
        elif pin == uBit.pin10:
            shift = 30
        elif pin == uBit.pin12:
            shift = 12
        elif pin == uBit.pin13:
            shift = 17
        elif pin == uBit.pin14:
            shift = 1
        elif pin == uBit.pin15:
            shift = 13
        # con't find pin16
        else:
            raise ValueError('function not suitable for this pin')

        return shift

    @staticmethod
    @micropython.asm_thumb
    def _block_irq():
        cpsid('i')          # disable interrupts to go really fast

    @staticmethod
    @micropython.asm_thumb
    def _unblock_irq():
        cpsie('i')          # enable interupts nolonger time critical

    # r0 - pin bit id
    # r1 - byte array
    # r2 - len byte array, must be a multiple of 4
    @staticmethod
    @micropython.asm_thumb
    def _grab_bits(r0, r1, r2):
        b(START)

        # DELAY routine
        label(DELAY)
        mov(r7, 0xa7)
        label(delay_loop)
        sub(r7, 1)
        bne(delay_loop)
        bx(lr)

        label(READ_PIN)
        mov(r3, 0x50)      # r3=0x50
        lsl(r3, r3, 16)    # r3=0x500000
        add(r3, 0x05)      # r3=0x500005
        lsl(r3, r3, 8)     # r3=0x50000500 -- this points to GPIO registers
        add(r3, 0x10)      # r3=0x50000510 -- points to read_digital bits
        ldr(r4, [r3, 0])   # move memory@r3 to r2
        mov(r3, 0x01)      # create bit mask in r3
        lsl(r3, r0)        # select bit from r0
        and_(r4, r3)
        lsr(r4, r0)
        bx(lr)

        label(START)
        mov(r5, 0x00)      # r5 - byte array index
        label(again)
        mov(r6, 0x00)      # r6 - current word
        bl(READ_PIN)
        orr(r6,  r4)       # bitwise or the pin into current word
        bl(DELAY)
        bl(READ_PIN)
        lsl(r4, r4, 8)     # move it left 1 byte
        orr(r6,  r4)       # bitwise or the pin into current word
        bl(DELAY)
        bl(READ_PIN)
        lsl(r4, r4, 16)     # move it left 2 bytes
        orr(r6,  r4)       # bitwise or the pin into current word
        bl(DELAY)
        bl(READ_PIN)
        lsl(r4, r4, 24)     # move it left 3 bytes
        orr(r6,  r4)       # bitwise or the pin into current word
        bl(DELAY)

        add(r1, r1, r5)   # add the index to the bytearra addres
        str(r6, [r1, 0])  # now 4 have been read store it
        sub(r1, r1, r5)   # reset the address
        add(r5, r5, 4)    # increase array index
        sub(r4, r2, r5)   # r4 - is now beig used to count bytes written
        bne(again)

        label(RETURN)
        mov(r0, r5)       # return number of bytes written

    @staticmethod
    def _parse_data(buffer_):

        max_bits = 50
        bits = bytearray(max_bits)
        length = 0
        bit_ = 0
        init = True

        for current in buffer_:

            if current == 1:
                length += 1
            elif bit_ == 0 and length == 0:
                pass
            elif init:
                length = 0
                init = False
            elif bit_ >= max_bits:
                pass
            elif length > 0:
                bits[bit_] = length
                length = 0
                bit_ += 1

        if bit_ == 0:
            return None

        results = bytearray(bit_)
        for i in range(bit_):
            results[i] = bits[i]
        return results

    @staticmethod
    def _calc_bytes(pull_up_lengths):

        shortest = 1000
        longest = 0

        for i in range(0, len(pull_up_lengths)):
            length = pull_up_lengths[i]
            if length < shortest:
                shortest = length
            if length > longest:
                longest = length

        halfway = shortest + (longest - shortest) / 2
        data = bytearray(5)
        did = 0
        byte = 0

        for i in range(len(pull_up_lengths)):
            byte = byte << 1

            if pull_up_lengths[i] > halfway:
                byte = byte | 1

            if ((i + 1) % 8 == 0):
                data[did] = byte
                did += 1
                byte = 0

        return data

    @staticmethod
    def _calc_checksum(data):
        return data[0] + data[1] + data[2] + data[3] & 0xff
