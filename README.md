# Repository evaluation pilot

Private synthetic repository for testing repository intake, historical task
construction and access isolation. This is authored demo code, not client code
or evidence of an actual customer incident.

The reservation helper determines whether a reservation remains active.
A reservation expires at its deadline: it is active only before `expires_at`.
All times are integer seconds in the same time basis.

Run the dependency-free tests with `python3 -m unittest discover -s tests -v`.
The initial historical version intentionally contains a boundary bug. A labeled
synthetic repair PR adds the missing regression case. Do not treat that seeded
history as naturally occurring engineering work or a held-out benchmark.

There are no deployment credentials, workflows, external services or client data.
Two-user access and GitHub App authorization still require real sign-ins.
