# Lab Run Report - Step 9: Hybrid Search + Reranking

## Target Query
> Evaluate quick ratio compliance against policy using combined retrieval.

## Retrieved Chunks
- **Source:** policy | **Score:** 10.00
  - *Excerpt:* Internal Liquidity Policy Statement: The mandatory minimum quick ratio floor for taking long position exposures is 1.00x. Any ratio between 1.00x and 1.15x requires active hedging and heightened executive monitoring. A quick ratio strictly above 1.15x is considered fully clear for open market long positions without mandatory hedging.
- **Source:** 10-K | **Score:** 9.00
  - *Excerpt:* FY2024 Revenue was $612.4M, representing an 18% increase year-over-year.  Gross Margin for FY2024 expanded to 43.1% from 40.2% in FY2023.  Diluted EPS for FY2024 reached $1.92 per share.  Debt Covenants require maintaining a minimum quick ratio of 1.00x at the end of each quarter.


## Model Output Answer
Compliance for quick ratio requirements draws on two distinct thresholds that must both be considered together.

From a debt covenant standpoint, the requirement is a minimum quick ratio of 1.00x maintained at the end of each quarter. This represents the baseline compliance threshold tied to contractual debt obligations.

From an internal risk management standpoint, the standard is stricter and more nuanced:

- A quick ratio below 1.00x fails compliance entirely — long position exposures are not permitted.
- A quick ratio between 1.00x and 1.15x technically satisfies the mandatory floor but falls into a cautionary zone, requiring active hedging strategies and heightened executive-level monitoring.
- Only a quick ratio strictly above 1.15x is considered fully clear, allowing open market long positions without any mandatory hedging requirement.

When evaluating compliance holistically, meeting the 1.00x debt covenant alone is insufficient for full risk clearance. A company or position could be in technical covenant compliance while still sitting in the elevated-risk band (1.00x–1.15x) internally, triggering additional hedging and oversight obligations. True unrestricted compliance — satisfying both the covenant and the internal risk appetite without added controls — requires the quick ratio to exceed 1.15x.

Therefore, compliance should be assessed on a tiered basis: below 1.00x is a breach of both covenant and policy; between 1.00x and 1.15x is covenant-compliant but policy-restricted (hedging and monitoring required); and above 1.15x is fully compliant under both frameworks with no additional restrictions.


