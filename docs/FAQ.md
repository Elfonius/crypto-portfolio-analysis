# FAQ

## Is this investment advice?

No. It is a review framework and a calculation helper. It does not know your full financial situation, tax position, or legal constraints. It flags issues for you and your advisers.

## Does it connect to my wallet?

Only if your agent has a read-only data source for the address. The skill itself does not request keys or sign. Prefer public addresses or exported positions. Never paste a seed phrase.

## Does it execute trades?

No. There is no signing, approval, swap, bridge, deposit, or order path. That is a hard boundary, not a configuration option.

## Which chains and assets are supported?

The method is chain-agnostic. Actual coverage depends on the data source and the agent’s tools. EVM chains, Solana, and Bittensor are common, but a position that cannot be resolved exactly must be marked `not assessable`.

## Why is there no single “portfolio score”?

A single score hides the trade-off between concentration, liquidity, tail risk, and return. The skill reports a dashboard and named flags instead.

## Why no target price?

A target price is a forecast, not evidence. The skill uses scenarios, ranges, and falsifiers. It may discuss valuation, but it does not present a target as fact.

## Why is VaR not enough?

VaR can understate extreme events, ignores liquidity, and is sensitive to correlation and regime. The skill adds CVaR, stress, reverse stress, and liquidity stress.

## Does it use Dune, Token Terminal, or Glassnode?

Only if the user has keys and the source answers in the current session. They are not assumed. The default source set is free/public where possible.

## Why Turkish and English templates?

The repository documentation is English for portability. The Turkish templates serve users who want a plain-language report. The method is the same.

## Does it store my data?

The skill is files and instructions. Your agent may write local reports or caches; check your agent’s privacy settings. Do not commit wallet data or API keys to a public repository.

## How do I add a new chain or protocol?

Add a reference with exact contract/market resolution, a source probe, and a failure mode. Add a fixture if the math changes. Run the tests and validator.

## Can I use it commercially?

Yes, under the MIT license. Keep the copyright notice and do not present it as a guarantee.
