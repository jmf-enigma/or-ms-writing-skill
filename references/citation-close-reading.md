# Citation Close Reading

Use this when checking whether a citation, related-work sentence, contribution claim, referee response, or literature contrast is substantively correct. This is about content fit, not citation formatting.

## Nonnegotiable Rule

Do not decide that a citation is appropriate from the title, abstract, metadata, BibTeX, cited-by count, or memory alone. Metadata verifies identity. It does not verify that the cited paper supports the sentence.

If the current sentence relies on a cited paper, read the relevant content of that paper:

1. Abstract and introduction positioning.
2. The section that contains the cited object: model, data, empirical design, theorem, proof idea, result table, mechanism test, robustness check, or appendix.
3. Conclusion or discussion only when the current sentence cites implications or boundary.
4. Appendix or online companion when the cited claim is technical, proof-based, measurement-based, or robustness-based.

If the full text is inaccessible, say the citation support is unverified. Do not write as if the paper has been checked.

## Citation Fit Map

For each cited paper, record five local facts before using it:

- **Object**: what decision, setting, model, data, theorem, mechanism, or construct the paper actually studies.
- **Support type**: theory, empirical design, structural estimate, algorithmic guarantee, simulation, experiment, review, or conceptual argument.
- **Main claim used here**: the exact result or argument from the cited paper that the current sentence needs.
- **Boundary**: assumptions, sample, setting, policy class, model regime, identification condition, or benchmark.
- **Fit**: whether the citation supports background, method precedent, benchmark, contrast, mechanism, empirical fact, proof technique, or novelty boundary.

Only cite a paper for the role it can actually play.

## Common Misfits

- A paper studies the same topic but not the same mechanism.
- A theory paper gives a model intuition, but the sentence cites it as empirical evidence.
- An empirical paper documents association, but the sentence cites it as causal evidence.
- A method paper introduces a tool, but the sentence cites it as proof that the tool works in this setting.
- A paper's abstract sounds close, but the result section addresses a different unit, metric, treatment, or benchmark.
- A citation cluster is used after a broad sentence without saying what the stream actually established.
- A novelty claim says "first" or "new" without checking whether prior work studied the same object under another name.

## How To Write After Reading

Good citation prose attaches the citation to a narrow claim:

- `Prior work studies [object] under [assumption or setting].`
- `[Author-year] estimates [effect] using [design] in [setting].`
- `[Stream] characterizes [formal object], whereas our setting adds [information, constraint, timing, or benchmark].`
- `This paper differs from [stream] in [decision, data source, mechanism, proof technique, or performance criterion].`

Avoid:

- `A large literature studies this problem.`
- `Prior work provides important insights.`
- `This paper fills a gap in the literature.`
- citation lists that replace explanation.

## Verification Boundary

Use an available citation lookup tool for metadata, BibTeX, DOI, author-year, and cited-by checks. Use browsing or supplied PDFs/full text to verify what the cited paper actually says. When exact wording matters, quote only short compliant excerpts and otherwise paraphrase.
