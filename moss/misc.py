"""Miscellaneous utility functions."""
import numpy as np
from IPython.core.display import Javascript, display


def make_master_schedule(evs):
    """Take a list of event specifications and make one schedule.

    Parameters
    ----------
    evs : sequence of n x 3 arrays
        list of (onset, duration, amplitude) event secifications

    Returns
    -------
    sched : n_event x 5 array
        schedule of event specifications with
        event and presentation ids

    """
    evs = np.asarray(evs)
    n_cond = len(evs)

    # Make a vector of condition ids and stimulus indices
    cond_ids = [np.ones(evs[i].shape[0]) * i for i in range(n_cond)]
    cond_ids = np.concatenate(cond_ids)
    stim_idxs = np.concatenate([np.arange(len(ev)) for ev in evs])

    # Make a schedule of the whole run
    sched = np.row_stack(evs)
    sched = np.column_stack((sched, cond_ids, stim_idxs))

    # Sort the master schedule by onset time
    timesorter = np.argsort(sched[:, 0])
    sched = sched[timesorter]
    return sched


def save_notebook():
    """Save an IPython notebook from running code.

    Note this must be returned from a notebook cell.

    """
    display(Javascript('IPython.notebook.save_notebook()'))


def sig_stars(p):
    """Return a R-style significance string corresponding to p values."""
    if p < 0.001:
        return "***"
    elif p < 0.01:
        return "**"
    elif p < 0.05:
        return "*"
    elif p < 0.1:
        return "."
    return ""
