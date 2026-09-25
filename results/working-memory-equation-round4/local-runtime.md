# Observed local runtime

The frozen selected equation analyzed20 previously unseen development passages in this fresh process. Full per-passage analysis took a median **1.131 seconds** (mean1.166; range0.955–1.500). These calls included whole-passage grammar extraction, text measurements, the runner’s model reload/decoding, numerical prediction and output checks. The first passage took1.500 seconds. The20 passages contained179 reading steps.

Before the passage calls, separate setup measurements were: runner import0.033s; selected predictor import0.349s; parser factory setup2.956s; integrity/dependency check1.080s. A separate model-decoding probe took0.512s. **These probes are not added to per-call times as an ordinary invocation**; the shipped runner reloads the model within every timed call. Some lazy word-table setup can remain in the first passage call.

Running the same passages again took a median0.927s. That repeat pass can reuse cached text measurements, so it is reported separately and is not the speed for analyzing new text. The outputs were identical.

The sample was fixed before model selection from the200 new development passages:8 passages of45–70words,8 of80–115words, and4 of130–170words, one per scenario family. Seeded ID hashes selected and ordered the sample without reference scores. This is a descriptive convenience benchmark, not a representative timing estimate or an accuracy test.

Inference ran in one relocated process with networking and all original workspace/app paths denied. Only the selected equation was evaluated. Architecture:arm64; Python3.9.6. Operating-system disk caches were not flushed; background workloads were not controlled. Timings describe this machine and run, not universal speed or a comparison with Jev latency. No API requests were made.
