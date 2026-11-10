# Dataset Card — Default of Credit Card Clients

## Dataset Identity

**Name:** Default of Credit Card Clients

**Provider:** UCI Machine Learning Repository

**UCI Dataset ID:** 350

**DOI:** 10.24432/C55S3H

**Original research:**  
Yeh, I.-C., & Lien, C.-H. (2009). *The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients.*

**Official source:**  
UCI Machine Learning Repository — Default of Credit Card Clients

## License

The UCI repository identifies this dataset as licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

The project will retain appropriate attribution to the original dataset and research.

## Dataset Description

The dataset contains information about credit card clients and is intended for classification of whether a client will default on the following month's payment.

The UCI repository reports:

- 30,000 observations
- 23 predictive features
- Integer and real-valued variables
- A binary target
- No missing values in the published dataset

The dataset contains information relating to:

- Credit limit
- Demographic attributes
- Age
- Historical repayment status
- Monthly bill statements
- Previous payment amounts

## Target Variable

The prediction target represents whether the client defaulted on the following month's payment.

For modeling, the target will be represented as a binary variable:

```text
0 = no default
1 = default
```

The exact target-column name and raw encoding will be verified during ingestion rather than assumed by downstream components.

## Feature Groups

The original dataset contains the following broad feature groups.

### Credit Information

- Credit limit

### Demographic Information

- Sex
- Education
- Marital status
- Age

### Repayment History

Six months of repayment-status information.

These variables describe historical payment behavior, including payment delays.

### Bill Statements

Six months of bill-statement amounts.

### Previous Payments

Six months of previous-payment amounts.

## Data Quality Considerations

Although the UCI metadata reports no missing values, absence of null values does not imply that the dataset is automatically clean.

The ingestion and validation pipeline will explicitly inspect:

- Column names
- Data types
- Duplicate records
- Identifier uniqueness
- Target encoding
- Class distribution
- Numeric ranges
- Categorical domains
- Unexpected category values
- Negative values
- Extreme values
- Potential data-entry anomalies
- Feature-target leakage risks

Some categorical codes require careful interpretation against the original documentation.

For example, the published data contains categorical values that are not fully explained by the simplified category descriptions in the documentation.

These values will not be silently removed or reassigned.

Instead, their treatment will be:

1. identified during profiling;
2. documented;
3. validated through automated checks;
4. handled explicitly in the feature-processing pipeline.

## Repayment Status Encoding

The original documentation describes repayment-status values using codes representing payment behavior.

The project will preserve the original values in the raw dataset.

Any transformation into a more convenient representation will occur in a separate processing layer and will be documented and tested.

The raw source data will never be silently overwritten.

## Intended Use

This dataset will be used for:

- Educational machine learning development
- Risk-model experimentation
- Model evaluation
- Explainability research
- Fairness analysis
- Model validation demonstrations
- MLOps experimentation
- Monitoring demonstrations
- Model-governance workflow demonstrations

The project is intended to demonstrate engineering and analytical techniques rather than produce a deployable financial decision system.

## Out-of-Scope Uses

This project must not be represented as:

- A production credit decision system
- A source of financial advice
- A real-world lending decision service
- A substitute for regulatory or legal review
- A validated model for use with real customers
- Evidence that a particular demographic group should receive different financial treatment

Model outputs from this project must not be used to make actual lending or credit decisions.

## Fairness Considerations

The dataset contains demographic attributes including sex, education, marital status, and age.

These variables provide an opportunity to demonstrate group-level model evaluation and responsible-AI techniques.

Fairness analysis will be treated as an analytical exercise rather than as a claim that the dataset's categories correspond exactly to legally protected characteristics in every jurisdiction.

The project will evaluate questions such as:

- Does predictive performance differ across groups?
- Do error rates differ across groups?
- Do selection or predicted-risk rates differ?
- How do fairness metrics change when the classification threshold changes?
- What trade-offs exist between predictive performance and fairness metrics?

Fairness metrics will not be interpreted in isolation.

## Privacy Considerations

The dataset contains historical client-level financial and demographic attributes.

Although the dataset is publicly available through the UCI Machine Learning Repository, the project will treat the information as sensitive in nature.

The repository will:

- Use the dataset only for the documented educational purposes
- Avoid attempting to identify individuals
- Avoid enriching records with external personal information
- Avoid publishing additional personal information
- Avoid using the dataset for real-world decision-making

The raw dataset will not be committed to Git.

## Reproducibility

The data-ingestion process will be designed to make dataset acquisition reproducible.

The project will document:

- Source location
- Dataset identifier
- DOI
- License
- Acquisition method
- Source filename
- File checksum where appropriate
- Processing steps
- Schema expectations
- Validation results

Raw and processed data will remain outside Git version control.

## Data Lineage

The intended lineage is:

```text
UCI Machine Learning Repository
            │
            ▼
       Raw dataset
            │
            ▼
    Ingestion validation
            │
            ▼
   Canonical tabular data
            │
            ▼
   Feature engineering
            │
            ▼
       ML datasets
            │
            ▼
     Model development
```

Every transformation should be reproducible from the documented source data and project code.

## Known Limitations

Important limitations include:

- The dataset represents a historical population and financial environment.
- The data originates from Taiwan and should not automatically be assumed representative of other populations or jurisdictions.
- Historical relationships in the data may not remain stable over time.
- The dataset does not represent a modern production lending environment.
- Dataset variables and categorical encodings may contain ambiguities requiring explicit treatment.
- Model performance on this dataset does not establish production suitability.
- Fairness results are dataset- and methodology-specific.

## Model-Risk Considerations

The project will explicitly distinguish between:

**Predictive performance**

and

**Model suitability for a decision context.**

A model with strong ROC-AUC or accuracy may still have important weaknesses involving:

- Calibration
- Threshold selection
- Data quality
- Feature stability
- Distribution shift
- Fairness
- Explainability
- Operational constraints
- Model assumptions
- Validation evidence

These considerations will become inputs to the later model-validation and governance components.

## Attribution

Dataset attribution:

> Yeh, I.-C. (2009). Default of Credit Card Clients [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C55S3H

The dataset is provided under the Creative Commons Attribution 4.0 International license.

## Source Verification

The dataset metadata and licensing information were verified against the UCI Machine Learning Repository before implementation.

The project should periodically verify the upstream dataset metadata rather than assuming that third-party mirrors remain authoritative.