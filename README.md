## Credit Scoring Business Understanding

This section establishes the regulatory, financial, and operational frameworks governing the risk classification structures developed in this repository. 

### 1. Basel II Accord Regulations & The Imperative for Interpretability
The Basel II Accord (and its subsequent Basel III/IV evolutionary layers) fundamentally shifted global banking operations by tying a financial institution's capital reserve requirements directly to the mathematically quantified risks of its asset portfolio. Under the **Internal Ratings-Based (IRB)** approach, institutions are empowered to use empirical internal models to estimate critical credit metrics: **Probability of Default (PD)**, **Loss Given Default (LGD)**, and **Exposure at Default (EAD)**.

Because these parameters determine exactly how much capital an institution must maintain on its balance sheet as a cushion against unexpected losses, regulators place a strict mandate on high interpretability and exhaustive documentation rather than permitting opaque "black-box" models:

* **Supervisory Validation and Stress Testing (Pillar 2):** Central bank examiners and internal risk validation teams must inspect the model's structural mechanics. If a model's feature relationships cannot be explicitly audited line-by-line, supervisors cannot verify if the risk weights will remain structurally sound or behave erratically during macroeconomic downturns.
* **Capital Reserve Justification:** An artificial drop in a bank's risk calculations directly lowers its required capital reserves, boosting short-term profitability but exposing the broader economy to systemic shock. Comprehensive documentation proves to regulators that your feature engineering, outlier transformations, and weight assignments reflect genuine underlying risk rather than statistical manipulation to bypass reserve requirements.
* **The "Right to an Explanation" and Consumer Protection:** Under modern fair lending standards and consumer credit guidelines, an institution must be capable of providing clear, actionable adverse action reasons to any consumer denied credit. An interpretable model isolates the exact feature thresholds responsible for a low credit score, shielding the company from compliance penalties and fair-lending litigation.

---

### 2. Proxy Target Variables and Associated Business Risks
In conventional retail credit scoring, models are trained on rich historical portfolios spanning multiple years, where accounts are explicitly labeled with mature financial default definitions (e.g., standard Basel definitions like 90+ days past due). However, in digital fintech micro-lending platforms, transaction-focused setups, or newly launched credit facilities, a direct historical "default" label is often missing or unavailable.

To bridge this data gap and train a predictive classifier, a **Proxy Target Variable** must be engineered (such as identifying specific transactional velocity collapses, severe balance drawdowns, or operational timing anomalies). While necessary to jumpstart predictive modeling, relying on a proxy variable introduces significant underlying business risks:

* **Label Misclassification & Credit Rationing (False Positives):** A proxy variable can mistakenly capture benign behavioral anomalies instead of genuine financial distress. For example, a reliable small merchant experiencing a brief, seasonal supply-chain payment delay might be flagged as "high-risk." This leads to unnecessary credit rejections, causing missed revenue opportunities and an artificial increase in customer churn.
* **Adverse Selection & Non-Performing Loans (False Negatives):** Conversely, if the engineered proxy is too permissive or misaligned with actual insolvency dynamics, fundamentally high-risk borrowers will clear the underwriting model's thresholds. This leads directly to elevated capital charge-offs, collection costs, and an inflation of Non-Performing Loans (NPLs) that harms the institution's financial health.
* **Target Disconnect (Concept Drift):** Consumer habits, operational products, and macroeconomic contexts change over time. If the correlation between your engineered proxy (e.g., wallet velocity anomalies) and true loan repayment behavior weakens, the model will continue optimizing for a target variable that no longer reflects actual credit default risk.

---

### 3. Key Model Trade-offs in Regulated Environments
Deploying machine learning models within regulated environments requires balancing predictive performance against institutional and regulatory compliance:

| Evaluation Aspect | Parametric Scorecards <br>*(e.g., Logistic Regression with Weight of Evidence - WoE)* | Advanced Ensemble Models <br>*(e.g., Gradient Boosting / XGBoost)* |
| :--- | :--- | :--- |
| **Explainability & Transparency** | **Maximum.** Continuous attributes are binned into monotonic Weight of Evidence (WoE) groups, converting feature relationships into clear log-odds. Every variable has an explicit scorecard points allocation easily understood by underwriters, risk officers, and auditors. | **Low to Moderate.** Operates through deep, nested, non-linear tree structures. Requires secondary post-hoc interpretability wrappers (such as SHAP or LIME values) to approximate feature contributions, adding operational complexity during regulatory audits. |
| **Predictive Performance** | **Moderate.** Relies heavily on manual feature engineering. Because it models linear relationships, it can miss subtle, non-linear multi-variable interactions unless explicitly specified by the data analyst. | **Superior.** Highly capable of automatically capturing deep interactive patterns, non-linear boundaries, and complex mathematical dependencies across attributes without manual data preparation. |
| **Regulatory & Compliance Alignment** | **High & Streamlined.** Standard WoE-based Logistic Regression models are widely accepted across international banking frameworks and line-by-line validation procedures. | **Challenging.** Often requires additional documentation, rigorous adversarial testing, and proof of algorithmic stability to ensure the model does not introduce systemic bias or volatile shifts under market stress. |
| **Operational Robustness** | **Excellent.** WoE feature binning naturally insulates the model from the impacts of missing values, out-of-range outliers, and data noise, making it highly stable over time. | **High Vulnerability to Overfitting.** If regularized improperly, ensemble models can memorize background historical noise rather than genuine credit behaviors, requiring rigorous hyperparameter monitoring. |

#### Tactical Strategy
To achieve both objectives, institutions often adopt a **Dual-Model Champion-Challenger Strategy**: utilizing a high-performance Gradient Boosting model as an analytical benchmark to uncover new non-linear feature insights, while deploying a transparent, audited WoE Logistic Regression model as the production underwriting engine to satisfy compliance and documentation mandates.
