// ============================================================
// BASIC ELEMENTS
// ============================================================

const imageInput = document.getElementById("imageInput");
const leafPreview = document.getElementById("leafPreview");
const imagePlaceholder = document.getElementById("imagePlaceholder");

const analyzeButton = document.getElementById("analyzeButton");
const loadingMessage = document.getElementById("loadingMessage");

const waitingResult = document.getElementById("waitingResult");
const resultContent = document.getElementById("resultContent");


// ============================================================
// MAIN RESULT ELEMENTS
// ============================================================

const disease = document.getElementById("disease");
const confidence = document.getElementById("confidence");
const affectedArea = document.getElementById("affectedArea");

const healthScore = document.getElementById("healthScore");
const healthBar = document.getElementById("healthBar");

const severity = document.getElementById("severity");
const status = document.getElementById("status");

const lastScan = document.getElementById("lastScan");
const plantStatus = document.getElementById("plantStatus");
const currentDate = document.getElementById("currentDate");


// ============================================================
// FARMER ALERT ELEMENTS
// ============================================================

const farmerAlert = document.getElementById("farmerAlert");

const farmerAlertHeading =
    document.getElementById("farmerAlertHeading");

const farmerAlertTitle =
    document.getElementById("farmerAlertTitle");

const farmerAffectedArea =
    document.getElementById("farmerAffectedArea");

const farmerSeverity =
    document.getElementById("farmerSeverity");


// ============================================================
// LANGUAGE BUTTONS
// ============================================================

const englishButton =
    document.getElementById("englishButton");

const hindiButton =
    document.getElementById("hindiButton");


// ============================================================
// LABELS
// ============================================================

const affectedAreaLabel =
    document.getElementById("affectedAreaLabel");

const severityLabel =
    document.getElementById("severityLabel");

const aboutDiseaseHeading =
    document.getElementById("aboutDiseaseHeading");

const causeLabel =
    document.getElementById("causeLabel");

const symptomsLabel =
    document.getElementById("symptomsLabel");

const spreadLabel =
    document.getElementById("spreadLabel");

const conditionsLabel =
    document.getElementById("conditionsLabel");

const actionsHeading =
    document.getElementById("actionsHeading");

const sprayHeading =
    document.getElementById("sprayHeading");

const additionalActionHeading =
    document.getElementById("additionalActionHeading");

const warningHeading =
    document.getElementById("warningHeading");


// ============================================================
// FARMER CONTENT
// ============================================================

const farmerMessageSection =
    document.getElementById("farmerMessageSection");

const farmerMessage =
    document.getElementById("farmerMessage");

const aboutDiseaseSection =
    document.getElementById("aboutDiseaseSection");

const causeText =
    document.getElementById("causeText");

const symptomsText =
    document.getElementById("symptomsText");

const spreadText =
    document.getElementById("spreadText");

const conditionsText =
    document.getElementById("conditionsText");

const actionsList =
    document.getElementById("actionsList");

const lowMessageSection =
    document.getElementById("lowMessageSection");

const lowMessage =
    document.getElementById("lowMessage");

const spraySection =
    document.getElementById("spraySection");

const sprayList =
    document.getElementById("sprayList");

const additionalActionSection =
    document.getElementById("additionalActionSection");

const additionalActionText =
    document.getElementById("additionalActionText");

const farmerWarning =
    document.getElementById("farmerWarning");


// ============================================================
// STORED RESULT
// ============================================================

let latestResult = null;

let currentLanguage = "en";


// ============================================================
// CURRENT DATE
// ============================================================

const today = new Date();

currentDate.textContent = today.toLocaleDateString(
    "en-IN",
    {
        day: "2-digit",
        month: "short",
        year: "numeric"
    }
);


// ============================================================
// IMAGE PREVIEW
// ============================================================

imageInput.addEventListener(
    "change",
    function () {

        const file =
            imageInput.files[0];

        if (!file) {
            return;
        }

        const imageURL =
            URL.createObjectURL(file);

        leafPreview.src =
            imageURL;

        leafPreview.style.display =
            "block";

        imagePlaceholder.style.display =
            "none";


        // Hide old result when selecting
        // a new image.

        waitingResult.classList.remove(
            "hidden"
        );

        resultContent.classList.add(
            "hidden"
        );

        farmerAlert.classList.add(
            "hidden"
        );

        loadingMessage.textContent =
            "";
    }
);


// ============================================================
// LANGUAGE BUTTONS
// ============================================================

englishButton.addEventListener(
    "click",
    function () {

        currentLanguage = "en";

        updateLanguageButtons();

        displayFarmerAlert();
    }
);


hindiButton.addEventListener(
    "click",
    function () {

        currentLanguage = "hi";

        updateLanguageButtons();

        displayFarmerAlert();
    }
);


// ============================================================
// UPDATE LANGUAGE BUTTON STYLE
// ============================================================

function updateLanguageButtons() {

    englishButton.classList.remove(
        "active"
    );

    hindiButton.classList.remove(
        "active"
    );


    if (currentLanguage === "en") {

        englishButton.classList.add(
            "active"
        );

    } else {

        hindiButton.classList.add(
            "active"
        );
    }
}


// ============================================================
// UPDATE LANGUAGE LABELS
// ============================================================

function updateLanguageLabels() {

    if (currentLanguage === "hi") {

        farmerAlertHeading.textContent =
            "⚠️ किसान चेतावनी";

        affectedAreaLabel.textContent =
            "प्रभावित क्षेत्र:";

        severityLabel.textContent =
            "गंभीरता:";

        aboutDiseaseHeading.textContent =
            "📖 रोग विवरण";

        causeLabel.textContent =
            "कारण:";

        symptomsLabel.textContent =
            "लक्षण:";

        spreadLabel.textContent =
            "फैलाव:";

        conditionsLabel.textContent =
            "अनुकूल परिस्थितियाँ:";

        actionsHeading.textContent =
            "🌱 आपको क्या करना चाहिए?";

        sprayHeading.textContent =
            "🧴 अनुशंसित छिड़काव";

        additionalActionHeading.textContent =
            "⚠️ अतिरिक्त उपाय";

        warningHeading.textContent =
            "महत्वपूर्ण:";

    } else {

        farmerAlertHeading.textContent =
            "⚠️ FARMER ALERT";

        affectedAreaLabel.textContent =
            "Affected Area:";

        severityLabel.textContent =
            "Severity:";

        aboutDiseaseHeading.textContent =
            "📖 About the Disease";

        causeLabel.textContent =
            "Cause:";

        symptomsLabel.textContent =
            "Symptoms:";

        spreadLabel.textContent =
            "Spread:";

        conditionsLabel.textContent =
            "Favorable Conditions:";

        actionsHeading.textContent =
            "🌱 What Should You Do?";

        sprayHeading.textContent =
            "🧴 Recommended Spray";

        additionalActionHeading.textContent =
            "⚠️ Additional Action";

        warningHeading.textContent =
            "Important:";
    }
}


// ============================================================
// DISPLAY FARMER ALERT
// ============================================================

function displayFarmerAlert() {

    if (!latestResult) {
        return;
    }

    updateLanguageLabels();


    const farmerInfo =
        latestResult.farmer_info;


    // ========================================================
    // FARMER INFO NOT AVAILABLE
    // ========================================================

    if (
        !farmerInfo ||
        farmerInfo.available !== true
    ) {

        farmerAlert.classList.remove(
            "hidden"
        );

        farmerAlertTitle.textContent =
            currentLanguage === "hi"
                ? "परिणाम अनिश्चित है"
                : "Prediction Uncertain";

        farmerAffectedArea.textContent =
            `${Number(
                latestResult.affected_area_percent
            ).toFixed(2)}%`;

        farmerSeverity.textContent =
            latestResult.severity;

        farmerMessageSection.classList.remove(
            "hidden"
        );

        farmerMessage.textContent =
            currentLanguage === "hi"
                ? (
                    "AI का विश्वास कम है। "
                    + "कृपया पत्ती की साफ और स्पष्ट तस्वीर लेकर "
                    + "फिर से जांच करें।"
                )
                : (
                    "AI prediction confidence is low. "
                    + "Please capture a clearer tomato leaf "
                    + "image and analyze it again."
                );


        aboutDiseaseSection.classList.add(
            "hidden"
        );

        lowMessageSection.classList.add(
            "hidden"
        );

        spraySection.classList.add(
            "hidden"
        );

        additionalActionSection.classList.add(
            "hidden"
        );

        actionsList.innerHTML = "";

        farmerWarning.textContent =
            currentLanguage === "hi"
                ? "स्पष्ट परिणाम मिलने से पहले किसी उपचार का निर्णय न लें।"
                : "Do not make a treatment decision until a clear prediction is available.";

        return;
    }


    // ========================================================
    // GET SELECTED LANGUAGE DATA
    // ========================================================

    const languageData =
        farmerInfo.languages[
            currentLanguage
        ];


    if (!languageData) {
        return;
    }


    farmerAlert.classList.remove(
        "hidden"
    );


    // ========================================================
    // BASIC FARMER ALERT RESULT
    // ========================================================

    farmerAlertTitle.textContent =
        languageData.alert_title ||
        languageData.disease_name ||
        latestResult.prediction;


    farmerAffectedArea.textContent =
        `${Number(
            latestResult.affected_area_percent
        ).toFixed(2)}%`;


    farmerSeverity.textContent =
        latestResult.severity;


    // ========================================================
    // HEALTHY LEAF
    // ========================================================

    if (
        latestResult.prediction === "Healthy"
    ) {

        aboutDiseaseSection.classList.add(
            "hidden"
        );

        lowMessageSection.classList.add(
            "hidden"
        );

        spraySection.classList.add(
            "hidden"
        );

        additionalActionSection.classList.add(
            "hidden"
        );


        // Show healthy message.

        farmerMessageSection.classList.remove(
            "hidden"
        );


        let healthyMessage =
            languageData.message || "";


        if (languageData.treatment) {

            healthyMessage +=
                ` ${languageData.treatment}`;
        }


        farmerMessage.textContent =
            healthyMessage;


        // Healthy actions

        displayActions(
            languageData.actions || []
        );


        farmerWarning.textContent =
            languageData.warning || "";


        return;
    }


    // ========================================================
    // DISEASE
    // ========================================================

    farmerMessageSection.classList.add(
        "hidden"
    );


    aboutDiseaseSection.classList.remove(
        "hidden"
    );


    const about =
        languageData.about || {};


    causeText.textContent =
        about.cause || "--";

    symptomsText.textContent =
        about.symptoms || "--";

    spreadText.textContent =
        about.spread || "--";

    conditionsText.textContent =
        about.favorable_conditions || "--";


    // ========================================================
    // ACTIONS
    // ========================================================

    displayActions(
        languageData.actions || []
    );


    // ========================================================
    // LOW SEVERITY
    // ========================================================

    if (
        String(
            latestResult.severity
        ).toUpperCase() === "LOW"
    ) {

        lowMessageSection.classList.remove(
            "hidden"
        );

        lowMessage.textContent =
            languageData.message ||
            (
                currentLanguage === "hi"
                    ? (
                        "प्रभावित क्षेत्र 10% से कम है। "
                        + "अभी स्प्रे की सलाह नहीं दी जाती।"
                    )
                    : (
                        "Affected area is below 10%. "
                        + "No spray is recommended at this stage."
                    )
            );


        spraySection.classList.add(
            "hidden"
        );

        additionalActionSection.classList.add(
            "hidden"
        );
    }


    // ========================================================
    // MODERATE OR HIGH
    // ========================================================

    else {

        lowMessageSection.classList.add(
            "hidden"
        );


        const sprays =
            languageData.sprays || [];


        if (sprays.length > 0) {

            spraySection.classList.remove(
                "hidden"
            );

            displaySprays(
                sprays
            );

        } else {

            spraySection.classList.add(
                "hidden"
            );

            sprayList.innerHTML =
                "";
        }


        // ====================================================
        // HIGH ADDITIONAL ACTION
        // ====================================================

        if (
            languageData.additional_action
        ) {

            additionalActionSection.classList.remove(
                "hidden"
            );

            additionalActionText.textContent =
                languageData.additional_action;

        } else {

            additionalActionSection.classList.add(
                "hidden"
            );
        }
    }


    // ========================================================
    // WARNING
    // ========================================================

    farmerWarning.textContent =
        languageData.warning || "";
}


// ============================================================
// DISPLAY ACTIONS
// ============================================================

function displayActions(actions) {

    actionsList.innerHTML = "";


    actions.forEach(
        function (action) {

            const li =
                document.createElement("li");

            li.textContent =
                action;

            actionsList.appendChild(
                li
            );
        }
    );
}


// ============================================================
// DISPLAY SPRAYS
// ============================================================

function displaySprays(sprays) {

    sprayList.innerHTML = "";


    sprays.forEach(
        function (spray, index) {

            const card =
                document.createElement("div");

            card.className =
                "spray-card";


            // =========================
            // SPRAY NAME
            // =========================

            const title =
                document.createElement("h5");

            title.textContent =
                `${index + 1}. ${spray.name || "Spray"}`;


            // =========================
            // ACTIVE INGREDIENT
            // =========================

            const ingredient =
                document.createElement("p");

            ingredient.className =
                "spray-ingredient";


            ingredient.innerHTML =
                currentLanguage === "hi"
                    ? (
                        "<strong>सक्रिय घटक:</strong> "
                        + (
                            spray.active_ingredient ||
                            "--"
                        )
                    )
                    : (
                        "<strong>Active Ingredient:</strong> "
                        + (
                            spray.active_ingredient ||
                            "--"
                        )
                    );


            // =========================
            // INSTRUCTIONS
            // =========================

            const instructions =
                document.createElement("p");

            instructions.textContent =
                spray.instructions || "";


            // =========================
            // SPRAY LINK
            // =========================

            card.appendChild(
                title
            );

            card.appendChild(
                ingredient
            );

            card.appendChild(
                instructions
            );


            if (spray.url) {

                const link =
                    document.createElement("a");

                link.href =
                    spray.url;

                link.target =
                    "_blank";

                link.rel =
                    "noopener noreferrer";

                link.className =
                    "spray-link";

                link.textContent =
                    currentLanguage === "hi"
                        ? "स्प्रे की जानकारी देखें"
                        : "View Spray Information";

                card.appendChild(
                    link
                );
            }


            sprayList.appendChild(
                card
            );
        }
    );
}


// ============================================================
// ANALYZE IMAGE
// ============================================================

analyzeButton.addEventListener(
    "click",
    async function () {

        const file =
            imageInput.files[0];


        if (!file) {

            alert(
                "Please select a tomato leaf image first."
            );

            return;
        }


        // ====================================================
        // LOADING STATE
        // ====================================================

        analyzeButton.disabled =
            true;

        analyzeButton.textContent =
            "Analyzing...";

        loadingMessage.textContent =
            "AI is analyzing the tomato leaf...";


        // ====================================================
        // FORM DATA
        // ====================================================

        const formData =
            new FormData();

        formData.append(
            "file",
            file
        );


        try {

            // =================================================
            // SEND IMAGE TO FASTAPI
            // =================================================

            const response =
                await fetch(
                    "http://127.0.0.1:8000/upload",
                    {
                        method: "POST",
                        body: formData
                    }
                );


            const data =
                await response.json();


            // =================================================
            // API ERROR
            // =================================================

            if (
                !response.ok ||
                data.error
            ) {

                throw new Error(
                    data.error ||
                    "Unable to analyze image."
                );
            }


            // =================================================
            // SAVE RESULT
            // =================================================

            latestResult =
                data;


            // Every new result starts
            // in English.

            currentLanguage =
                "en";

            updateLanguageButtons();


            // =================================================
            // AFFECTED AREA
            // =================================================

            const affected =
                Number(
                    data.affected_area_percent
                );


            // =================================================
            // HEALTH SCORE
            // =================================================

            let calculatedHealth;


            if (
                data.health_score_percent !==
                undefined
            ) {

                calculatedHealth =
                    Number(
                        data.health_score_percent
                    );

            } else {

                calculatedHealth =
                    Math.max(
                        0,
                        Math.min(
                            100,
                            100 - affected
                        )
                    );
            }


            // =================================================
            // DISPLAY MAIN RESULTS
            // =================================================

            disease.textContent =
                data.prediction.replaceAll(
                    "_",
                    " "
                );


            confidence.textContent =
                `${Number(
                    data.confidence
                ).toFixed(2)}%`;


            affectedArea.textContent =
                `${affected.toFixed(2)}%`;


            healthScore.textContent =
                `${calculatedHealth.toFixed(2)}%`;


            healthBar.style.width =
                `${calculatedHealth}%`;


            severity.textContent =
                data.severity;


            status.textContent =
                data.status;


            // =================================================
            // SEVERITY BADGE
            // =================================================

            severity.classList.remove(
                "severity-low",
                "severity-moderate",
                "severity-high"
            );


            const severityValue =
                String(
                    data.severity
                ).toUpperCase();


            if (
                severityValue === "LOW" ||
                severityValue === "VERY LOW"
            ) {

                severity.classList.add(
                    "severity-low"
                );

            }

            else if (
                severityValue === "MODERATE"
            ) {

                severity.classList.add(
                    "severity-moderate"
                );

            }

            else if (
                severityValue === "HIGH"
            ) {

                severity.classList.add(
                    "severity-high"
                );
            }


            // =================================================
            // SUMMARY CARDS
            // =================================================

            const now =
                new Date();


            lastScan.textContent =
                now.toLocaleTimeString(
                    [],
                    {
                        hour: "2-digit",
                        minute: "2-digit"
                    }
                );


            plantStatus.textContent =
                data.status;


            // =================================================
            // SHOW MAIN RESULT
            // =================================================

            waitingResult.classList.add(
                "hidden"
            );


            resultContent.classList.remove(
                "hidden"
            );


            // =================================================
            // SHOW FARMER ALERT
            // =================================================

            displayFarmerAlert();


            loadingMessage.textContent =
                "Analysis completed successfully.";
        }


        catch (error) {

            console.error(
                error
            );


            loadingMessage.textContent =
                "Could not connect to the AI server.";


            alert(
                "Analysis failed. Make sure FastAPI is running."
            );
        }


        finally {

            analyzeButton.disabled =
                false;


            analyzeButton.textContent =
                "Analyze Leaf";
        }
    }
);