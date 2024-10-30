package main

import (
	"context"
	"fmt"
	"time"
)

func handleMultipleChannels(
	ctx context.Context,
	ch1, ch2 <-chan string,
	timeout time.Duration,
) (string, error) {
	timeoutCh := time.After(timeout)

	for {
		select {
		case <-ctx.Done():
			return "", ctx.Err() // Handles context cancellation

		case msg1, ok := <-ch1:
			if !ok {
				// Channel closed
				ch1 = nil // // Disable this case to prevent repeated selects on a closed channel
				continue
			}
			return fmt.Sprintf("Ch1: %s", msg1), nil

		case msg2, ok := <-ch2:
			if !ok {
				ch2 = nil
				continue
			}
			return fmt.Sprintf("Ch2: %s", msg2), nil

		case <-timeoutCh:
			return "", fmt.Errorf("timeout after %v", timeout)
		}
	}
}

func main() {
	ctx := context.Background()
	ch1 := make(chan string)
	ch2 := make(chan string)
	handleMultipleChannels(ctx, ch1, ch2, time.Duration(2))
}
/*
Why This Pattern is Important:
Non-blocking handling of multiple channels: 
The select statement enables the function to wait for multiple channels at once, ensuring non-blocking handling of incoming data.
Graceful handling of closed channels: When a channel is closed, setting it to nil removes it from future select cases, preventing errors from repeated reads on a closed channel.
Timeout mechanism: The time.After channel enforces a timeout, ensuring the function returns if no messages arrive within the specified duration.
Context cancellation support: The ctx.Done() case respects external cancellation signals, providing controlled shutdown and resource cleanup.
Avoids goroutine leaks: Proper handling of timeouts and context cancellation prevents goroutines from running indefinitely, avoiding potential memory and resource leaks.
*/