from scripts.check_docs_plans import checkout_steps_disable_persisted_credentials


CHECKOUT = "actions/checkout@df4cb1c069e1874edd31b4311f1884172cec0e10"


def test_checkout_step_disables_persisted_credentials():
    workflow = f"""
jobs:
  verify:
    steps:
      - name: Checkout
        uses: {CHECKOUT}
        with:
          persist-credentials: false
      - run: make check
"""

    assert checkout_steps_disable_persisted_credentials(workflow)


def test_checkout_comment_cannot_spoof_credential_isolation():
    workflow = f"""
jobs:
  verify:
    steps:
      - name: Checkout
        uses: {CHECKOUT}
        # persist-credentials: false
      - run: make check
"""

    assert not checkout_steps_disable_persisted_credentials(workflow)


def test_unrelated_step_cannot_spoof_credential_isolation():
    workflow = f"""
jobs:
  verify:
    steps:
      - name: Checkout
        uses: {CHECKOUT}
      - name: Unrelated
        run: echo ok
        with:
          persist-credentials: false
"""

    assert not checkout_steps_disable_persisted_credentials(workflow)


def test_every_checkout_step_must_disable_persisted_credentials():
    workflow = f"""
jobs:
  verify:
    steps:
      - uses: {CHECKOUT}
        with:
          persist-credentials: false
      - uses: {CHECKOUT}
"""

    assert not checkout_steps_disable_persisted_credentials(workflow)


def test_duplicate_checkout_input_cannot_override_isolation():
    workflow = f"""
jobs:
  verify:
    steps:
      - uses: {CHECKOUT}
        with:
          persist-credentials: false
          persist-credentials: true
"""

    assert not checkout_steps_disable_persisted_credentials(workflow)


def test_workflow_without_checkout_is_rejected():
    assert not checkout_steps_disable_persisted_credentials("jobs: {}\n")
