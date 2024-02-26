import usb.core as core
import usb.util
from time import sleep

TOYPAD_INIT = [0x55, 0x0f, 0xb0, 0x01, 0x28, 0x63, 0x29, 0x20, 0x4c, 0x45, 0x47, 0x4f, 0x20, 0x32, 0x30, 0x31, 0x34, 0xf7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

OFF = [0, 0, 0]

ALL_PADS = 0

def init_usb():
    global dev

    dev = core.find(idVendor=0x0e6f, idProduct=0x0241)

    if dev is None:
        print('Device not found')
    else:
        if dev.is_kernel_driver_active(0):
            dev.detach_kernel_driver(0)

        print(usb.util.get_string(dev, dev.iProduct))

        dev.set_configuration()
        dev.write(1, TOYPAD_INIT)

    return dev

def send_command(dev, command):
    # calculate checksum
    checksum = sum(command) % 256
    message = command + [checksum]

    # pad message
    while len(message) < 32:
        message.append(0x00)

    # send message
    dev.write(1, message)

    return

def switch_pad(pad, colour):
    send_command(dev, [0x55, 0x06, 0xc0, 0x02, pad, colour[0], colour[1], colour[2]])
    return

def lerp_color(start, end, t):
    return [int(start[i] + t * (end[i] - start[i])) for i in range(3)]

def switch_pad_smoothly(pad, start_color, end_color, duration):
    steps = 500  # Number of steps for smooth transition
    time_step = duration / steps

    for step in range(steps):
        t = step / float(steps - 1)
        interpolated_color = lerp_color(start_color, end_color, t)
        switch_pad(pad, interpolated_color)
        sleep(time_step)

def main():
    init_usb()

    start_color = [65, 0, 0]  # Start with red
    end_color = [0, 0, 65]    # Transition to blue
    transition_duration = 600    # Transition duration in seconds

    while True:
        switch_pad_smoothly(ALL_PADS, start_color, end_color, transition_duration)
        switch_pad_smoothly(ALL_PADS, end_color, start_color, transition_duration)

if __name__ == '__main__':
    main()
