import time
import threading
import schedule

from TP_lib import gt1151

import hardware
from state import State
from view import View

def main(events_file, missed_file):
    state = State()
    view = View()

    def TouchThread():
        gt = gt1151.GT1151()
        gt.GT_Init()
        touch_data_old = gt1151.GT_Development()
        touch_data_new = gt1151.GT_Development()
        drawn =done = False
        while True:
            if gt.digital_read(gt.INT) == 0:
                touch_data_new.Touch = 1
            else:
                touch_data_new.Touch = 0
            gt.GT_Scan(touch_data_new, touch_data_old)

            if coming and not done:
                if not drawn:
                    view.DisplayEvent(state.upcoming.message)
                    drawn = True
                if touch_data_new.S[0] > 64:
                    view.DisplayTime()
                    hardware.Rotate(17, 45)
                    done = True
                else:
                    state.WriteMissed()

            else:
                done = False
                if touch_data_new.S[0] > 64:
                    view.DisplayLatest(state.latest.time, state.latest.message)

            time.sleep(0.1)

    t = threading.Thread(target=TouchThread)
    t.daemon = True
    t.start()

    try:
        while True:
            coming = False
            state.UpdateEvents(events_file)

            if state.upcoming.time < time.time() + 60:
                coming = True
                time.sleep(60)
        
            else:
                view.DisplayTime()
                time.sleep(10)
                view.DisplayUpcoming(state.upcoming.time)
                time.sleep(10)

    finally:
        schedule.clear()
        view.Shutdown()

if __name__ == "__main__":
    main("demo.json", "missed.json")