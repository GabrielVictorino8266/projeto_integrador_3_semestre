import { useRef, useState } from 'react';

export function useDelayedSpinner(delayMs: number = 200) {
  const [visible, setVisible] = useState(false);
  const timeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const cancelledRef = useRef(false);

  function start() {
    cancelledRef.current = false;

    timeoutRef.current = setTimeout(() => {
      if (!cancelledRef.current) {
        setVisible(true);
      }
    }, delayMs);
  }

  function stop() {
    cancelledRef.current = true;
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current);
      timeoutRef.current = null;
    }
    setVisible(false);
  }

  return {
    showSpinner: visible,
    startSpinner: start,
    stopSpinner: stop
  };
}
