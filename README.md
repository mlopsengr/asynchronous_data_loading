# Logic Breakdown
This explains the processes performed in the data_loading.py file within the package folder in a high level. The code can be adapted for specific use cases.

## Cloud Database Simulation
- `CLOUD_DB_ENDPOINTS`: A list of simulated dummy cloud database endpoints.
- `fetch_data_from_cloud_db(session, url, queue)`: An asynchronous function that fetches data from a cloud database and puts it in the queue. This function simulates fetching new data every 1 to 3 seconds.


## Data Processing
- `process_data(queue, stop_event)`: A background task that processes data from the queue. It processes data at random intervals between 0.1 to 0.5 seconds. It runs until the stop_event is set and the queue is empty.
- `stop_event` is set and the queue is empty.

## The Main application
 - `main()`:
    - Sets up the queue and the stop event.
    - Creates tasks for fetching data from each cloud database endpoint and a task for processing data.
    - Simulates running the main application for 20 seconds.
    - Sets the stop event to signal the data processing task to stop.
    - Cancels the fetching tasks and waits for the queue to be fully processed before stopping the data processing task.
