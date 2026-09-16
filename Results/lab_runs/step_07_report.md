# Lab Run Report - Step 7: Hybrid Search (Dense + Sparse Fusion)

## Target Query
> How does the quick ratio from earnings call align with internal policy?

## Retrieved Chunks
- **Source:** 10-K | **Score:** 0.07
  - *Excerpt:* FY2024 Revenue was $612.4M, representing an 18% increase year-over-year.  Gross Margin for FY2024 expanded to 43.1% from 40.2% in FY2023.  Diluted EPS for FY2024 reached $1.92 per share.  Debt Covenants require maintaining a minimum quick ratio of 1.00x at the end of each quarter.
- **Source:** call | **Score:** 0.07
  - *Excerpt:* During Q3, our quick ratio improved from 1.18x in the prior quarter to 1.23x as of Q3 end. We are confident in our liquidity position and our ability to remain well above the floor required by our financial covenants.
- **Source:** policy | **Score:** 0.07
  - *Excerpt:* Internal Liquidity Policy Statement: The mandatory minimum quick ratio floor for taking long position exposures is 1.00x. Any ratio between 1.00x and 1.15x requires active hedging and heightened executive monitoring. A quick ratio strictly above 1.15x is considered fully clear for open market long positions without mandatory hedging.


## Model Output Answer
The quick ratio reported at the end of Q3, 1.23x, sits comfortably above the 1.15x threshold defined in the internal liquidity policy. This means the company is considered fully clear for open market long positions without requiring mandatory hedging. It also exceeds the mandatory minimum floor of 1.00x tied to the debt covenants by a healthy margin, and surpasses the 1.15x level that would otherwise trigger active hedging and heightened executive monitoring. The improvement from 1.18x in the prior quarter to 1.23x further reinforces that the company has moved further away from the heightened-monitoring band and into the fully clear zone under the internal policy.


