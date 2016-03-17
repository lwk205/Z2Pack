#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    08.02.2016 15:02:23 CET
# File:    _result.py

from .._result import Result

class SurfaceResult(Result):
    """TODO"""
    
    @property
    def convergence_report(self):
        r"""
        Returns a convergence report (as a string) for the result. This report shows whether the convergence options used for calculating this result were satisfied or not.
        """
        def section_heading(name):
            return name + '\n' + '=' * len(name) + '\n\n'
        
        def ctrl_heading(ctrl):
            return ctrl.__name__ + '\n' + '-' * len(ctrl.__name__) + '\n\n'
        
        line_report = []
        line_c_ctrl = set()
        for line in self.lines:
            line_c_ctrl.update(line.ctrl_convergence.keys())
        for c_ctrl in sorted(list(line_c_ctrl), key=lambda x: x.__name__):
            failed_t = []
            inexistent_t = []
            for line in self.lines:
                try:
                    if not line.ctrl_convergence[c_ctrl]:
                        failed_t.append(line.t)
                except KeyError:
                    inexistent_t.append(line.t)
            report_entry = ctrl_heading(c_ctrl)
            if failed_t:
                report_entry += 'Failed instances at t = ' + str(failed_t) + '\n\n'
            else:
                report_entry += 'All instances passed.\n\n'
            if inexistent_t:
                report_entry += 'Missing instances at t = ' + str(inexistent_t) + '\n\n'
            else:
                report_entry += 'No missing instances.\n\n'
            line_report.append(report_entry)

        report = section_heading('Line Convergence')
        report += ''.join(line_report) + '\n'

        report += section_heading('Surface Convergence')

        surface_report = []
        for c_ctrl, converged in sorted(self.ctrl_convergence.items(), key=lambda x: x[0].__name__):
            report_entry = ctrl_heading(c_ctrl)
            if converged is None:
                report_entry += 'Convergence test has not run!'
            else:
                failed = [
                    t_pair
                    for t_pair, conv in zip(zip(self.t[:-1], self.t[1:]), converged)
                    if not conv
                ]
                if failed:
                    report_entry += 'Failed for the following pairs (t1, t2) = ' + str(failed)
                else:
                    report_entry += 'All instances passed.'
            report_entry += '\n\n'
            report += report_entry
        
        return report