# What did “verified” verify?

**Bounded public-source reading · November 13, 2026**

This is a routine editor-task case to test the [November 11 distinction](recovery-and-outcome-scope-2026-11-11.md)
between an action and the purpose it serves. VS Code contributors added an announcement for the current line and column. A user described needing the position while switching to a coding assistant. That is a reported use case, not an AI intervention or an observed workflow result. See the [eight records](position-and-shortcut-records-2026-11-13.json) and [source register](sources-2026-11-13.json).

| Purpose | Evidence observed | What remains open |
|---|---|---|
| Hear the correct location | The [column patch](https://github.com/microsoft/vscode/pull/286412) accounts for tabs. The [January 8 check](https://github.com/microsoft/vscode/issues/278855#issuecomment-3722883129) confirms the column correction in that test. | Correctness across environments was not established. |
| Invoke the announcement by keyboard | The same check reports that the old shortcut still failed on two Windows machines. A [later patch](https://github.com/microsoft/vscode/pull/286586) changes the Windows shortcut; a subsequent change specifies an accessibility-mode condition. | Earlier Windows reports differed. Team testing and source declarations do not establish runtime success for everyone. |
| Keep a separate route to source control | A [linked regression](https://github.com/microsoft/vscode/issues/286825) documents the competing use of the key. A [backport](https://github.com/microsoft/vscode/pull/286879) and pinned 1.108.1 source show distinct bindings. One [commenter](https://github.com/microsoft/vscode/issues/286825#issuecomment-3753650812) reports a successful check on that version in the regression thread. | Test procedure and configuration are unstated. That report does not confirm the new announcement, cumulative costs, or all users' experience. |

The original issue was closed, reopened after a failed check, closed again, and later labeled verified. The January 8 report is the decisive observation for this reading: two results coexist under that single status. January 9 already has a separate regression record, before a January 13 comment on the original issue. The timeline supports a separate design constraint; it does not prove that the later comment caused the fix.

For review, record a result against the **affected task, route, version, and configuration**. The result for one purpose does not fill the other cells. A contributor's report, merged code, a released source tag, and a user check answer different questions. The document trail shows proposed work, merges and reports, but does not establish exclusive authority, how many people bore extra work, or whether the combined change improved actual work overall.

AI assisted retrieval, comparison and writing. No editor test, original participant data or causal analysis was added. Researcher understanding and independent source/method review are pending. This is a proposed observation distinction; existing study designs and simulation code are unchanged.
