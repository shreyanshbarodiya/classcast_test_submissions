# classcast test submission

The APIs in this repository, are for Open edX platform.

## Endpoint: classcast/submission/newsubmission
### Params: POST request

student_id: pass as a param for now, after implementation of login, it will be fetched from session
xblock_id 
attempted: 1 for attempted/ 0 for skipped
correctly_attempted: (1 for correctly attempted) / (0 for incorrectly attempted & skipped)
time_taken: float value
timestamp: YYYY-MM-DD hh:mm:ss
appeared_in_test: (1 if appeared in test) / (0 if not appeared in test)
appeared_in_gym: (1 if appeared in gym) / (0 if not appeared in gym)
