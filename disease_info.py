# ============================================================
# FARMER-FRIENDLY DISEASE INFORMATION
# ============================================================
#
# PROJECT SEVERITY RULES
#
# 0% - <10%    = LOW
# 10% - <60%   = MODERATE
# 60% - 100%   = HIGH
#
# IMPORTANT:
# If AI predicts a disease but affected area is below 10%,
# the disease information and preventive actions can be shown,
# but NO spray is recommended.
#
# If AI predicts Healthy, the Healthy information is shown.
#
# ============================================================


DISEASE_INFO = {

    # ========================================================
    # HEALTHY
    # ========================================================

    "Healthy": {

        # ----------------------------------------------------
        # ENGLISH
        # ----------------------------------------------------

        "en": {
            "disease_name": "Healthy",

            "alert_title": "Healthy Leaf",

            "message": (
                "No significant disease was detected in the "
                "tomato leaf."
            ),

            "actions": [
                "Continue regular monitoring of the plant.",

                (
                    "Maintain proper watering and good field "
                    "hygiene."
                ),

                (
                    "Check the plant periodically for any new "
                    "spots, discoloration, or other symptoms."
                ),

                (
                    "Maintain good airflow between plants and "
                    "avoid unnecessary wetting of the leaves."
                )
            ],

            "treatment": (
                "No spray treatment is recommended at this stage."
            ),

            "warning": (
                "Continue monitoring the plant and take action "
                "if disease symptoms appear."
            )
        },


        # ----------------------------------------------------
        # HINDI
        # ----------------------------------------------------

        "hi": {
            "disease_name": "स्वस्थ",

            "alert_title": "स्वस्थ पत्ती",

            "message": (
                "टमाटर की पत्ती में कोई महत्वपूर्ण रोग नहीं "
                "पाया गया।"
            ),

            "actions": [
                "पौधे की नियमित निगरानी करते रहें।",

                (
                    "उचित सिंचाई और खेत की स्वच्छता बनाए रखें।"
                ),

                (
                    "समय-समय पर पत्तियों में नए धब्बे, रंग में "
                    "बदलाव या अन्य लक्षणों की जांच करें।"
                ),

                (
                    "पौधों के बीच हवा का अच्छा प्रवाह बनाए रखें "
                    "और पत्तियों को अनावश्यक रूप से गीला करने "
                    "से बचें।"
                )
            ],

            "treatment": (
                "इस अवस्था में किसी स्प्रे उपचार की आवश्यकता "
                "नहीं है।"
            ),

            "warning": (
                "पौधे की निगरानी जारी रखें और रोग के लक्षण "
                "दिखाई देने पर उचित कार्रवाई करें।"
            )
        }
    },


    # ========================================================
    # EARLY BLIGHT
    # ========================================================

    "Early_Blight": {

        # ----------------------------------------------------
        # ENGLISH
        # ----------------------------------------------------

        "en": {
            "disease_name": "Early Blight",

            "alert_title": "Early Blight Detected",

            "about": {
                "cause": (
                    "This disease is caused by a fungus called "
                    "Alternaria solani."
                ),

                "symptoms": (
                    "Circular brown or black spots begin to appear "
                    "on the older and lower leaves of the plant. "
                    "These spots often have target-like or "
                    "concentric ring patterns."
                ),

                "spread": (
                    "The disease starts from the lower part of the "
                    "plant and gradually spreads to the upper leaves, "
                    "stems, and fruits, which can cause significant "
                    "yield loss."
                ),

                "favorable_conditions": (
                    "The disease spreads rapidly in warm temperatures "
                    "(20°C–30°C) and humid or moist weather conditions."
                )
            },

            "actions": [
                (
                    "Apply mulch, such as dry grass or straw, around "
                    "the plants to prevent fungus-containing soil "
                    "particles from splashing onto the leaves through "
                    "water."
                ),

                (
                    "Remove and destroy infected leaves to prevent "
                    "the disease from spreading further."
                )
            ],


            # =================================================
            # MODERATE: 10% - <60%
            #
            # NOTE:
            # The information supplied in the source file was
            # labelled LOW. Our application maps this treatment
            # group to MODERATE.
            # =================================================

            "moderate_sprays": [

                {
                    "name": "Syngenta Amistar",

                    "active_ingredient": (
                        "Azoxystrobin 23% SC"
                    ),

                    "instructions": (
                        "Mix 1 ml per litre of water and spray. "
                        "It helps stop fungal growth."
                    ),

                    "url": (
                        "https://www.bighaat.com/products/"
                        "amistar-fungicide?pf=search"
                    )
                },

                {
                    "name": "BASF Merivon or Polyram",

                    "active_ingredient": (
                        "Metiram 55% + Pyraclostrobin 5% WG"
                    ),

                    "instructions": (
                        "Apply at a rate of 2 grams per litre "
                        "of water."
                    ),

                    "url": (
                        "https://www.bighaat.com/products/"
                        "cabrio-top-fungicide?pf=search"
                    )
                },

                {
                    "name": "Amistar Top",

                    "active_ingredient": (
                        "Azoxystrobin 18.2% + "
                        "Difenoconazole 11.4% SC"
                    ),

                    "instructions": (
                        "Mix 1 ml per litre of water and spray. "
                        "This fungicide is effective for controlling "
                        "the disease at a moderate stage."
                    ),

                    "url": (
                        "https://www.bighaat.com/products/"
                        "amistar-top-fungicide?pf=search"
                    )
                }
            ],


            # =================================================
            # HIGH: 60% - 100%
            # =================================================

            "high_sprays": [

                {
                    "name": "Bayer Nativo",

                    "active_ingredient": (
                        "Tebuconazole 50% + "
                        "Trifloxystrobin 25% WG"
                    ),

                    "instructions": (
                        "Mix 0.5 gram per litre of water "
                        "(or 100 grams per acre in 200 litres of water) "
                        "and spray. It is a powerful systemic fungicide."
                    ),

                    "url": (
                        "https://www.bighaat.com/products/"
                        "bayer-nativo-fungicide?pf=search"
                    )
                },

                {
                    "name": "Katyayani Dr. Blight",

                    "active_ingredient": (
                        "Metalaxyl-M 3.3% + "
                        "Chlorothalonil 33.1% SC"
                    ),

                    "instructions": (
                        "Apply at a rate of 2 ml per litre of water. "
                        "Its dual action (systemic and contact) helps "
                        "control severe infection rapidly."
                    ),

                    "url": (
                        "https://www.bighaat.com/products/"
                        "katyayani-dr-blight-metalaxyl-m-3-3-"
                        "chlorothalonil-33-1-sc?pf=search"
                    )
                },

                {
                    "name": "Adama Custodia",

                    "active_ingredient": (
                        "Azoxystrobin 11% + "
                        "Tebuconazole 18.3% SC"
                    ),

                    "instructions": (
                        "Apply at a rate of 200 ml per acre mixed "
                        "in 200 litres of water."
                    ),

                    "url": (
                        "https://www.bighaat.com/products/"
                        "adama-custodia-fungicide?pf=search"
                    )
                }
            ],

            "low_message": (
                "The visible affected area is below 10%. "
                "No spray is recommended at this stage. "
                "Follow the preventive actions and monitor "
                "the plant closely."
            ),

            "warning": (
                "Follow the product label instructions and local "
                "agricultural guidance."
            )
        },


        # ----------------------------------------------------
        # HINDI
        # ----------------------------------------------------

        "hi": {
            "disease_name": "अगेती झुलसा",

            "alert_title": "अगेती झुलसा रोग का पता चला",

            "about": {
                "cause": (
                    "यह बीमारी अल्टरनेरिया सोलानी "
                    "(Alternaria solani) नामक फफूंद "
                    "(कवक) के कारण होती है।"
                ),

                "symptoms": (
                    "इसमें पौधे की पुरानी और निचली पत्तियों पर "
                    "गोल, भूरे या काले रंग के धब्बे बनने लगते हैं। "
                    "इन धब्बों के अंदर लक्ष्य (target) या सांद्र "
                    "छल्ले (concentric rings) जैसी आकृतियाँ "
                    "दिखाई देती हैं।"
                ),

                "spread": (
                    "यह बीमारी नीचे से शुरू होकर धीरे-धीरे ऊपर की "
                    "पत्तियों, तनों और फलों तक फैल जाती है, जिससे "
                    "पैदावार को भारी नुकसान होता है।"
                ),

                "favorable_conditions": (
                    "यह गर्म (20°C से 30°C तापमान) और आर्द्र "
                    "(नमी वाले) मौसम में बहुत तेजी से फैलता है।"
                )
            },

            "actions": [
                (
                    "पौधे के आसपास गीली घास या पुआल (Mulching) "
                    "बिछाएं ताकि मिट्टी के फफूंद वाले कण पानी के "
                    "जरिए पत्तियों तक न पहुंच सकें।"
                ),

                (
                    "संक्रमित पत्तियों को तोड़कर नष्ट कर दें ताकि "
                    "बीमारी आगे न फैले।"
                )
            ],


            # =================================================
            # MODERATE: 10% - <60%
            # =================================================

            "moderate_sprays": [

                {
                    "name": "सिंजेंटा एमिस्टार",

                    "active_ingredient": (
                        "Azoxystrobin 23% SC"
                    ),

                    "instructions": (
                        "1 मिली प्रति लीटर पानी में मिलाकर स्प्रे करें। "
                        "यह फंगस की ग्रोथ को तुरंत रोकता है।"
                    ),

                    "url": (
                        "https://www.bighaat.com/products/"
                        "amistar-fungicide?pf=search"
                    )
                },

                {
                    "name": "बासएफ मेरीवॉन या पॉलीराम",

                    "active_ingredient": (
                        "Metiram 55% + Pyraclostrobin 5% WG"
                    ),

                    "instructions": (
                        "2 ग्राम प्रति लीटर पानी की दर से "
                        "छिड़काव करें।"
                    ),

                    "url": (
                        "https://www.bighaat.com/products/"
                        "cabrio-top-fungicide?pf=search"
                    )
                },

                {
                    "name": "एमिस्टार टॉप",

                    "active_ingredient": (
                        "Azoxystrobin 18.2% + "
                        "Difenoconazole 11.4% SC"
                    ),

                    "instructions": (
                        "1 मिली प्रति लीटर पानी में मिलाकर स्प्रे करें। "
                        "यह कवकनाशी मध्यम अवस्था के लिए बहुत असरदार है।"
                    ),

                    "url": (
                        "https://www.bighaat.com/products/"
                        "amistar-top-fungicide?pf=search"
                    )
                }
            ],


            # =================================================
            # HIGH: 60% - 100%
            # =================================================

            "high_sprays": [

                {
                    "name": "बायेर नेटिवो",

                    "active_ingredient": (
                        "Tebuconazole 50% + "
                        "Trifloxystrobin 25% WG"
                    ),

                    "instructions": (
                        "0.5 ग्राम प्रति लीटर पानी "
                        "(या 100 ग्राम प्रति एकड़ 200 लीटर पानी में) "
                        "मिलाकर छिड़काव करें। यह एक बेहद ताकतवर "
                        "सिस्टेमिक फंगीसाइड है।"
                    ),

                    "url": (
                        "https://www.bighaat.com/products/"
                        "bayer-nativo-fungicide?pf=search"
                    )
                },

                {
                    "name": "कात्यायनी डॉ. ब्लाइट",

                    "active_ingredient": (
                        "Metalaxyl-M 3.3% + "
                        "Chlorothalonil 33.1% SC"
                    ),

                    "instructions": (
                        "2 मिली प्रति लीटर पानी की दर से स्प्रे करें। "
                        "इसका दोहरा एक्शन (सिस्टेमिक और कॉन्टैक्ट) "
                        "भारी संक्रमण को तेजी से रोकता है।"
                    ),

                    "url": (
                        "https://www.bighaat.com/products/"
                        "katyayani-dr-blight-metalaxyl-m-3-3-"
                        "chlorothalonil-33-1-sc?pf=search"
                    )
                },

                {
                    "name": "Adama Custodia",

                    "active_ingredient": (
                        "Azoxystrobin 11% + "
                        "Tebuconazole 18.3% SC"
                    ),

                    "instructions": (
                        "200 मिली प्रति एकड़ की दर से 200 लीटर "
                        "पानी में घोलकर छिड़काव करें।"
                    ),

                    "url": (
                        "https://www.bighaat.com/products/"
                        "adama-custodia-fungicide?pf=search"
                    )
                }
            ],

            "low_message": (
                "दिखाई देने वाला प्रभावित क्षेत्र 10% से कम है। "
                "इस अवस्था में स्प्रे की सलाह नहीं दी जाती। "
                "दिए गए बचाव के उपाय अपनाएं और पौधे की नियमित "
                "निगरानी करें।"
            ),

            "warning": (
                "उत्पाद के लेबल पर दिए गए निर्देशों और स्थानीय "
                "कृषि विशेषज्ञों की सलाह का पालन करें।"
            )
        }
        },

    # ========================================================
    # BACTERIAL SPOT
    # ========================================================

    "Bacterial_Spot": {

        "en": {
            "disease_name": "Bacterial Spot",
            "alert_title": "Bacterial Spot Detected",

            "about": {
                "cause": (
                    "Bacterial spot of tomato is caused by several "
                    "species of Xanthomonas bacteria."
                ),

                "symptoms": (
                    "Small, dark brown to black spots appear on leaves. "
                    "Spots may develop yellow areas around them. "
                    "Infection can also produce raised or scabby spots "
                    "on fruits."
                ),

                "spread": (
                    "The bacteria spread through infected seed or "
                    "transplants, rain splash, irrigation water, "
                    "contaminated tools and handling of wet plants."
                ),

                "favorable_conditions": (
                    "Warm temperatures, high humidity, rainfall and "
                    "prolonged leaf wetness favor bacterial spot "
                    "development."
                )
            },

            "actions": [
                (
                    "Remove severely infected plant material and avoid "
                    "handling plants when the leaves are wet."
                ),
                (
                    "Avoid overhead irrigation and disinfect tools "
                    "used on infected plants."
                )
            ],

            "moderate_sprays": [
                {
                    "name": "Blitox",
                    "active_ingredient": "Copper Oxychloride 50% WP",
                    "instructions": (
                        "Copper-based contact treatment used for fungal "
                        "and bacterial diseases. BigHaat lists a general "
                        "dosage of 400 g/acre; use the tomato bacterial-"
                        "spot label rate."
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "tata-rallis-blitox-fungicide?pf=search"
                    )
                },

                {
                    "name": "Kocide 2000",
                    "active_ingredient": "Copper Hydroxide 53.8% DF",
                    "instructions": (
                        "A copper-based protective product used against "
                        "bacterial and fungal diseases. BigHaat gives a "
                        "general range of 400–600 g/acre; use only the "
                        "tomato label rate."
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "dupont-kocide-2000-fungicide-bactericide"
                    )
                }
            ],

            "high_sprays": [
                {
                    "name": "Dhanuka Conika",
                    "active_ingredient": (
                        "Kasugamycin 5% + Copper Oxychloride 45% WP"
                    ),
                    "instructions": (
                        "Fungicide-cum-bactericide with systemic and "
                        "contact action. BigHaat lists a general rate of "
                        "1.5 g/L or 300 g in 200 L water/acre, but its "
                        "listed crop recommendations do not specifically "
                        "include tomato; use it on tomato only if your "
                        "local product label permits."
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "conika-fungicide?pf=search"
                    )
                }
            ],

            "high_action": (
                "In severe bacterial spot, removing heavily infected "
                "tissue and preventing splash spread remain important. "
                "Do not simply increase the copper or bactericide "
                "concentration beyond the label rate."
            ),

            "low_message": (
                "The visible affected area is below 10%. "
                "No spray is recommended at this stage. "
                "Follow the preventive actions and monitor "
                "the plant closely."
            ),

            "warning": (
                "Follow the product label instructions and local "
                "agricultural guidance."
            )
        },


        # ----------------------------------------------------
        # HINDI
        # ----------------------------------------------------

        "hi": {
            "disease_name": "बैक्टीरियल स्पॉट",
            "alert_title": "बैक्टीरियल स्पॉट रोग का पता चला",

            "about": {
                "cause": (
                    "टमाटर का बैक्टीरियल स्पॉट रोग Xanthomonas समूह "
                    "के बैक्टीरिया के कारण होता है।"
                ),

                "symptoms": (
                    "पत्तियों पर छोटे, गहरे भूरे या काले धब्बे बनते हैं। "
                    "धब्बों के आसपास पीला क्षेत्र दिखाई दे सकता है। "
                    "फलों पर उभरे हुए या खुरदरे धब्बे भी बन सकते हैं।"
                ),

                "spread": (
                    "यह रोग संक्रमित बीज/पौध, बारिश की बूंदों, सिंचाई "
                    "के पानी, संक्रमित औजारों और गीले पौधों को छूने से "
                    "फैल सकता है।"
                ),

                "favorable_conditions": (
                    "गर्म तापमान, अधिक नमी, बारिश और लंबे समय तक "
                    "पत्तियों का गीला रहना रोग को बढ़ावा देता है।"
                )
            },

            "actions": [
                (
                    "अधिक संक्रमित हिस्सों को हटाकर नष्ट करें और "
                    "गीले पौधों को छूने से बचें।"
                ),
                (
                    "ऊपर से सिंचाई करने से बचें और संक्रमित पौधों पर "
                    "इस्तेमाल किए गए औजारों को साफ करें।"
                )
            ],

            "moderate_sprays": [
                {
                    "name": "Blitox",
                    "active_ingredient": "Copper Oxychloride 50% WP",
                    "instructions": (
                        "यह कॉपर आधारित कॉन्टैक्ट उत्पाद है। BigHaat पर "
                        "सामान्य मात्रा 400 ग्राम/एकड़ दी गई है; टमाटर "
                        "बैक्टीरियल स्पॉट के लिए लेबल मात्रा का पालन करें।"
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "tata-rallis-blitox-fungicide?pf=search"
                    )
                },

                {
                    "name": "Kocide 2000",
                    "active_ingredient": "Copper Hydroxide 53.8% DF",
                    "instructions": (
                        "यह कॉपर आधारित सुरक्षात्मक उत्पाद है। BigHaat "
                        "पर सामान्य मात्रा 400–600 ग्राम/एकड़ दी गई है। "
                        "टमाटर के लिए लेबल मात्रा का पालन करें।"
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "dupont-kocide-2000-fungicide-bactericide"
                    )
                }
            ],

            "high_sprays": [
                {
                    "name": "Dhanuka Conika",
                    "active_ingredient": (
                        "Kasugamycin 5% + Copper Oxychloride 45% WP"
                    ),
                    "instructions": (
                        "यह सिस्टेमिक + कॉन्टैक्ट फंगीसाइड-कम-"
                        "बैक्टीरिसाइड है। BigHaat पर सामान्य मात्रा "
                        "1.5 ग्राम/लीटर या 300 ग्राम/एकड़, 200 लीटर "
                        "पानी में दी गई है। BigHaat की सूची में टमाटर "
                        "इसकी स्पष्ट अनुशंसित फसल नहीं है, इसलिए टमाटर "
                        "पर केवल तभी उपयोग करें जब स्थानीय उत्पाद लेबल "
                        "इसकी अनुमति देता हो।"
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "conika-fungicide?pf=search"
                    )
                }
            ],

            "high_action": (
                "अधिक संक्रमण में संक्रमित हिस्सों को हटाना और पानी "
                "की छींटों से रोग के फैलाव को रोकना जरूरी है। लेबल से "
                "अधिक मात्रा में दवा न डालें।"
            ),

            "low_message": (
                "दिखाई देने वाला प्रभावित क्षेत्र 10% से कम है। "
                "इस अवस्था में स्प्रे की सलाह नहीं दी जाती। "
                "बचाव के उपाय अपनाएं और पौधे की नियमित निगरानी करें।"
            ),

            "warning": (
                "उत्पाद के लेबल पर दिए गए निर्देशों और स्थानीय "
                "कृषि विशेषज्ञों की सलाह का पालन करें।"
            )
        }
        },

    # ========================================================
    # LATE BLIGHT
    # ========================================================

    "Late_Blight": {

        # ----------------------------------------------------
        # ENGLISH
        # ----------------------------------------------------

        "en": {
            "disease_name": "Late Blight",
            "alert_title": "Late Blight Detected",

            "about": {
                "cause": (
                    "Late blight is caused by Phytophthora infestans, "
                    "a fungus-like microorganism (oomycete)."
                ),

                "symptoms": (
                    "Irregular, water-soaked, pale green to dark brown "
                    "spots appear on leaves. Under humid conditions, "
                    "white fungal-like growth may be visible on the "
                    "underside of infected leaves. Dark brown lesions "
                    "may also develop on stems and fruits."
                ),

                "spread": (
                    "The disease can spread very rapidly from infected "
                    "plants through wind-blown spores, rain splash and "
                    "moisture. Under favorable conditions, a large part "
                    "of the crop can become infected within a short period."
                ),

                "favorable_conditions": (
                    "Cool, cloudy and highly humid weather, frequent "
                    "rainfall and prolonged leaf wetness strongly favor "
                    "the disease."
                )
            },

            "actions": [
                (
                    "Remove and destroy severely infected leaves and "
                    "plants to reduce further spread."
                ),
                (
                    "Avoid overhead irrigation and unnecessary wetting "
                    "of leaves. Improve spacing and air circulation "
                    "around plants."
                )
            ],

            "moderate_sprays": [
                {
                    "name": "Blitox",
                    "active_ingredient": "Copper Oxychloride 50% WP",
                    "instructions": (
                        "A contact copper fungicide that provides "
                        "protective control against several fungal "
                        "diseases, including blight. Use according "
                        "to the tomato label."
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "tata-rallis-blitox-fungicide?pf=search"
                    )
                },

                {
                    "name": "Mancozeb 75% WP",
                    "active_ingredient": "Mancozeb 75% WP",
                    "instructions": (
                        "A broad-spectrum contact fungicide commonly "
                        "used as a protective treatment against blight "
                        "diseases. Follow the tomato label for dosage."
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "dhanuka-m45-fungicide?pf=search"
                    )
                },

                {
                    "name": "Syngenta Ridomil Gold",
                    "active_ingredient": (
                        "Metalaxyl-M 4% + Mancozeb 64% WP"
                    ),
                    "instructions": (
                        "A systemic + contact combination for oomycete "
                        "diseases. BigHaat lists 500–1000 g/acre as a "
                        "general dosage range; use only the crop-specific "
                        "label rate for tomato."
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "ridomill-gold-fungicide?pf=search"
                    )
                }
            ],

            "high_sprays": [
                {
                    "name": "BASF Acrobat",
                    "active_ingredient": "Dimethomorph 50% WP",
                    "instructions": (
                        "A systemic/translaminar fungicide used against "
                        "late blight. BigHaat lists a general rate of "
                        "approximately 1.3 g/L; use the tomato label "
                        "rate where registered."
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "acrobat-fungicide?pf=search"
                    )
                },

                {
                    "name": "Metalaxyl + Mancozeb",
                    "active_ingredient": (
                        "Metalaxyl 8% + Mancozeb 64% WP"
                    ),
                    "instructions": (
                        "BigHaat lists this combination for tomato late "
                        "blight at 800 g per acre in 200 litres of water."
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "exylon-matazeb-fungicide?pf=search"
                    )
                },

                {
                    "name": "Kocide 2000",
                    "active_ingredient": "Copper Hydroxide 53.8% DF",
                    "instructions": (
                        "A protective copper fungicide. BigHaat lists "
                        "400–600 g/acre as a general rate, but crop-specific "
                        "label directions must be followed."
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "tata-rallis-blitox-fungicide?pf=search"
                    )
                }
            ],

            "low_message": (
                "The visible affected area is below 10%. "
                "No spray is recommended at this stage. "
                "Follow the preventive actions and monitor "
                "the plant closely."
            ),

            "warning": (
                "Follow the product label instructions and local "
                "agricultural guidance."
            )
        },


        # ----------------------------------------------------
        # HINDI
        # ----------------------------------------------------

        "hi": {
            "disease_name": "पछेती झुलसा",
            "alert_title": "पछेती झुलसा रोग का पता चला",

            "about": {
                "cause": (
                    "यह रोग Phytophthora infestans नामक फफूंद जैसे "
                    "सूक्ष्मजीव (Oomycete) के कारण होता है।"
                ),

                "symptoms": (
                    "पत्तियों पर अनियमित, पानी से भीगे हुए जैसे हल्के "
                    "हरे से गहरे भूरे धब्बे दिखाई देते हैं। अधिक नमी "
                    "में पत्तियों के निचले भाग पर सफेद फफूंद जैसी परत "
                    "दिखाई दे सकती है। तनों और फलों पर भी गहरे भूरे "
                    "धब्बे बन सकते हैं।"
                ),

                "spread": (
                    "यह रोग संक्रमित पौधों से हवा, बारिश की बूंदों "
                    "और नमी के माध्यम से बहुत तेजी से फैल सकता है। "
                    "अनुकूल मौसम में कम समय में फसल का बड़ा हिस्सा "
                    "संक्रमित हो सकता है।"
                ),

                "favorable_conditions": (
                    "ठंडा, बादल वाला और अधिक नमी वाला मौसम, लगातार "
                    "बारिश तथा लंबे समय तक पत्तियों का गीला रहना रोग "
                    "के फैलाव को बढ़ाता है।"
                )
            },

            "actions": [
                (
                    "अधिक संक्रमित पत्तियों और पौधों को हटाकर नष्ट कर दें।"
                ),
                (
                    "ऊपर से पानी देने से बचें और पौधों के बीच उचित "
                    "दूरी रखकर हवा का प्रवाह बढ़ाएं।"
                )
            ],

            "moderate_sprays": [
                {
                    "name": "Blitox",
                    "active_ingredient": "Copper Oxychloride 50% WP",
                    "instructions": (
                        "यह एक कॉन्टैक्ट कॉपर फंगीसाइड है जो ब्लाइट "
                        "सहित कई फफूंद रोगों से सुरक्षा देता है। "
                        "टमाटर के लिए लेबल पर दी गई मात्रा का पालन करें।"
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "tata-rallis-blitox-fungicide?pf=search"
                    )
                },

                {
                    "name": "Mancozeb 75% WP",
                    "active_ingredient": "Mancozeb 75% WP",
                    "instructions": (
                        "यह एक ब्रॉड-स्पेक्ट्रम कॉन्टैक्ट फंगीसाइड है "
                        "जिसका उपयोग ब्लाइट रोगों से बचाव के लिए किया "
                        "जाता है। टमाटर के लेबल के अनुसार मात्रा का "
                        "उपयोग करें।"
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "dhanuka-m45-fungicide?pf=search"
                    )
                },

                {
                    "name": "Syngenta Ridomil Gold",
                    "active_ingredient": (
                        "Metalaxyl-M 4% + Mancozeb 64% WP"
                    ),
                    "instructions": (
                        "यह सिस्टेमिक + कॉन्टैक्ट फंगीसाइड संयोजन है। "
                        "BigHaat पर सामान्य मात्रा 500–1000 ग्राम/एकड़ "
                        "दी गई है; टमाटर के लिए केवल लेबल पर दी गई "
                        "मात्रा का उपयोग करें।"
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "ridomill-gold-fungicide?pf=search"
                    )
                }
            ],

            "high_sprays": [
                {
                    "name": "BASF Acrobat",
                    "active_ingredient": "Dimethomorph 50% WP",
                    "instructions": (
                        "यह लेट ब्लाइट के नियंत्रण के लिए उपयोग किया "
                        "जाने वाला सिस्टेमिक/ट्रांसलैमिनर फंगीसाइड है। "
                        "BigHaat पर सामान्य मात्रा लगभग 1.3 ग्राम/लीटर "
                        "दी गई है; टमाटर के लिए लेबल मात्रा का पालन करें।"
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "acrobat-fungicide?pf=search"
                    )
                },

                {
                    "name": "Metalaxyl + Mancozeb",
                    "active_ingredient": (
                        "Metalaxyl 8% + Mancozeb 64% WP"
                    ),
                    "instructions": (
                        "BigHaat पर टमाटर के लेट ब्लाइट के लिए इसकी "
                        "मात्रा 800 ग्राम प्रति एकड़, 200 लीटर पानी "
                        "में दी गई है।"
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "exylon-matazeb-fungicide?pf=search"
                    )
                },

                {
                    "name": "Kocide 2000",
                    "active_ingredient": "Copper Hydroxide 53.8% DF",
                    "instructions": (
                        "यह एक सुरक्षात्मक कॉपर फंगीसाइड है। BigHaat "
                        "पर सामान्य मात्रा 400–600 ग्राम/एकड़ दी गई है; "
                        "फसल-विशिष्ट लेबल निर्देशों का पालन करें।"
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "tata-rallis-blitox-fungicide?pf=search"
                    )
                }
            ],

            "low_message": (
                "दिखाई देने वाला प्रभावित क्षेत्र 10% से कम है। "
                "इस अवस्था में स्प्रे की सलाह नहीं दी जाती। "
                "बचाव के उपाय अपनाएं और पौधे की नियमित निगरानी करें।"
            ),

            "warning": (
                "उत्पाद के लेबल पर दिए गए निर्देशों और स्थानीय "
                "कृषि विशेषज्ञों की सलाह का पालन करें।"
            )
        }
        },

    # ========================================================
    # LEAF MOLD
    # ========================================================

    "Leaf_Mold": {

        # ----------------------------------------------------
        # ENGLISH
        # ----------------------------------------------------

        "en": {
            "disease_name": "Leaf Mold",
            "alert_title": "Leaf Mold Detected",

            "about": {
                "cause": (
                    "Tomato leaf mold is caused by the fungus "
                    "Passalora fulva (formerly Cladosporium fulvum)."
                ),

                "symptoms": (
                    "Pale green or yellow spots first appear on the "
                    "upper surface of older leaves. Olive-green to "
                    "brown, velvety fungal growth develops on the "
                    "underside of the leaves. Severely infected leaves "
                    "may curl, dry and die."
                ),

                "spread": (
                    "Spores spread from infected leaves to healthy "
                    "plants through wind, water splash, tools, workers "
                    "and infected plant material."
                ),

                "favorable_conditions": (
                    "High humidity, especially relative humidity above "
                    "about 85%, strongly favors the disease. Poor "
                    "ventilation and prolonged leaf wetness increase "
                    "infection."
                )
            },

            "actions": [
                (
                    "Remove and destroy infected leaves and crop debris."
                ),
                (
                    "Improve ventilation and plant spacing, and avoid "
                    "wetting the leaves while irrigating."
                )
            ],

            # =================================================
            # MODERATE: 10% - <60%
            # Source file called this LOW.
            # =================================================

            "moderate_sprays": [
                {
                    "name": "Syngenta Kavach",
                    "active_ingredient": "Chlorothalonil 75% WP",
                    "instructions": (
                        "A broad-spectrum contact fungicide that "
                        "inhibits fungal spore germination. BigHaat "
                        "lists a general dosage range of 1.25–2 g/L. "
                        "Use the crop-specific label rate."
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "kavach-fungicide?pf=search"
                    )
                },

                {
                    "name": "Blitox",
                    "active_ingredient": "Copper Oxychloride 50% WP",
                    "instructions": (
                        "A protective contact fungicide. Apply "
                        "according to the tomato label."
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "tata-rallis-blitox-fungicide?pf=search"
                    )
                }
            ],

            # =================================================
            # HIGH: 60% - 100%
            #
            # The supplied information does not specify a
            # particular high-stage product.
            # =================================================

            "high_sprays": [],

            "high_action": (
                "For established or severe leaf mold, use only a "
                "fungicide specifically registered on the product "
                "label for tomato leaf mold, and rotate modes of "
                "action where the label permits. Do not increase "
                "concentration simply because the affected "
                "percentage is high."
            ),

            "low_message": (
                "The visible affected area is below 10%. "
                "No spray is recommended at this stage. "
                "Follow the preventive actions and monitor "
                "the plant closely."
            ),

            "warning": (
                "Follow the product label instructions and local "
                "agricultural guidance."
            )
        },


        # ----------------------------------------------------
        # HINDI
        # ----------------------------------------------------

        "hi": {
            "disease_name": "पत्ती फफूंद",
            "alert_title": "पत्ती फफूंद रोग का पता चला",

            "about": {
                "cause": (
                    "टमाटर का लीफ मोल्ड रोग Passalora fulva "
                    "नामक फफूंद के कारण होता है।"
                ),

                "symptoms": (
                    "शुरुआत में पुरानी पत्तियों की ऊपरी सतह पर "
                    "हल्के हरे या पीले धब्बे दिखाई देते हैं। "
                    "पत्तियों के नीचे जैतूनी-हरे से भूरे रंग की "
                    "मखमली फफूंद बनती है। अधिक संक्रमण होने पर "
                    "पत्तियां मुड़कर सूख सकती हैं।"
                ),

                "spread": (
                    "रोग के बीजाणु हवा, पानी की बूंदों, औजारों, "
                    "काम करने वाले लोगों और संक्रमित पौधों के "
                    "अवशेषों से फैल सकते हैं।"
                ),

                "favorable_conditions": (
                    "अधिक नमी, विशेष रूप से लगभग 85% से अधिक "
                    "सापेक्ष आर्द्रता, रोग के तेजी से फैलने के लिए "
                    "अनुकूल होती है। खराब वेंटिलेशन और पत्तियों का "
                    "लंबे समय तक गीला रहना संक्रमण बढ़ाता है।"
                )
            },

            "actions": [
                (
                    "संक्रमित पत्तियों और पौधों के अवशेषों को "
                    "हटाकर नष्ट करें।"
                ),
                (
                    "पौधों के बीच हवा का प्रवाह बढ़ाएं और सिंचाई "
                    "करते समय पत्तियों को गीला करने से बचें।"
                )
            ],

            # =================================================
            # MODERATE: 10% - <60%
            # =================================================

            "moderate_sprays": [
                {
                    "name": "Syngenta Kavach",
                    "active_ingredient": "Chlorothalonil 75% WP",
                    "instructions": (
                        "यह एक ब्रॉड-स्पेक्ट्रम कॉन्टैक्ट फंगीसाइड है। "
                        "BigHaat पर सामान्य मात्रा 1.25–2 ग्राम/लीटर "
                        "दी गई है। फसल-विशिष्ट लेबल मात्रा का पालन करें।"
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "kavach-fungicide?pf=search"
                    )
                },

                {
                    "name": "Blitox",
                    "active_ingredient": "Copper Oxychloride 50% WP",
                    "instructions": (
                        "यह एक सुरक्षात्मक कॉन्टैक्ट फंगीसाइड है। "
                        "टमाटर के लेबल के अनुसार उपयोग करें।"
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "tata-rallis-blitox-fungicide?pf=search"
                    )
                }
            ],

            # =================================================
            # HIGH: 60% - 100%
            # =================================================

            "high_sprays": [],

            "high_action": (
                "अधिक संक्रमण में केवल उसी फंगीसाइड का उपयोग करें "
                "जिसके उत्पाद लेबल पर टमाटर लीफ मोल्ड के लिए स्पष्ट "
                "अनुमति हो। रोग अधिक होने पर अपनी ओर से दवा की "
                "सांद्रता न बढ़ाएं।"
            ),

            "low_message": (
                "दिखाई देने वाला प्रभावित क्षेत्र 10% से कम है। "
                "इस अवस्था में स्प्रे की सलाह नहीं दी जाती। "
                "बचाव के उपाय अपनाएं और पौधे की नियमित निगरानी करें।"
            ),

            "warning": (
                "उत्पाद के लेबल पर दिए गए निर्देशों और स्थानीय "
                "कृषि विशेषज्ञों की सलाह का पालन करें।"
            )
        }
        },

    # ========================================================
    # SEPTORIA LEAF SPOT
    # ========================================================

    "Septoria_Leaf_Spot": {

        # ----------------------------------------------------
        # ENGLISH
        # ----------------------------------------------------

        "en": {
            "disease_name": "Septoria Leaf Spot",
            "alert_title": "Septoria Leaf Spot Detected",

            "about": {
                "cause": (
                    "Septoria leaf spot is caused by the fungus "
                    "Septoria lycopersici."
                ),

                "symptoms": (
                    "Numerous small, round spots develop mainly on "
                    "older and lower leaves. The spots usually have "
                    "dark margins with gray or light-colored centers. "
                    "Tiny black fruiting bodies may become visible "
                    "in the center of the spots."
                ),

                "spread": (
                    "Spores spread mainly through splashing rain or "
                    "irrigation water from infected plant debris and "
                    "leaves. Contaminated tools and handling can also "
                    "contribute to spread."
                ),

                "favorable_conditions": (
                    "Warm, wet and humid conditions favor infection. "
                    "Frequent rainfall and prolonged leaf wetness can "
                    "cause rapid disease development."
                )
            },

            "actions": [
                (
                    "Remove infected lower leaves and old tomato "
                    "crop debris."
                ),
                (
                    "Avoid overhead watering, use mulch to reduce "
                    "soil splash, and improve airflow between plants."
                )
            ],

            # =================================================
            # MODERATE: 10% - <60%
            # Source file called this LOW.
            # =================================================

            "moderate_sprays": [
                {
                    "name": "Syngenta Kavach",
                    "active_ingredient": "Chlorothalonil 75% WP",
                    "instructions": (
                        "Broad-spectrum contact fungicide. BigHaat "
                        "lists a general dosage of 1.25–2 g/L. "
                        "Use the crop-specific label rate."
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "kavach-fungicide?pf=search"
                    )
                },

                {
                    "name": "Blitox",
                    "active_ingredient": "Copper Oxychloride 50% WP",
                    "instructions": (
                        "Protective contact fungicide that may be used "
                        "for leaf-spot diseases where permitted by "
                        "the tomato label."
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "tata-rallis-blitox-fungicide?pf=search"
                    )
                }
            ],

            # =================================================
            # HIGH: 60% - 100%
            # =================================================

            "high_sprays": [
                {
                    "name": "BASF Merivon",
                    "active_ingredient": (
                        "Fluxapyroxad 250 g/L + "
                        "Pyraclostrobin 250 g/L SC"
                    ),
                    "instructions": (
                        "BigHaat specifically lists tomato – Early "
                        "Blight & Septoria Leaf Spot at 80–100 ml "
                        "per acre in 200 litres of water."
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "merivon-fungicide?pf=search"
                    )
                }
            ],

            "high_action": (
                "For severe infection, remove badly infected leaves "
                "in addition to spraying and follow the labeled spray "
                "interval. Rotate fungicide modes of action where the "
                "label permits to reduce resistance risk."
            ),

            "low_message": (
                "The visible affected area is below 10%. "
                "No spray is recommended at this stage. "
                "Follow the preventive actions and monitor "
                "the plant closely."
            ),

            "warning": (
                "Follow the product label instructions and local "
                "agricultural guidance."
            )
        },


        # ----------------------------------------------------
        # HINDI
        # ----------------------------------------------------

        "hi": {
            "disease_name": "सेप्टोरिया लीफ स्पॉट",
            "alert_title": "सेप्टोरिया लीफ स्पॉट रोग का पता चला",

            "about": {
                "cause": (
                    "यह रोग Septoria lycopersici नामक फफूंद "
                    "के कारण होता है।"
                ),

                "symptoms": (
                    "मुख्य रूप से पुरानी और निचली पत्तियों पर बहुत "
                    "से छोटे गोल धब्बे दिखाई देते हैं। इन धब्बों के "
                    "किनारे गहरे रंग के और बीच का हिस्सा धूसर या "
                    "हल्के रंग का होता है। धब्बों के बीच छोटे काले "
                    "बिंदु भी दिखाई दे सकते हैं।"
                ),

                "spread": (
                    "संक्रमित पत्तियों और पौधों के अवशेषों से बीजाणु "
                    "बारिश या सिंचाई के पानी की छींटों के माध्यम से "
                    "फैलते हैं। संक्रमित औजार और पौधों को छूना भी "
                    "रोग के फैलाव में योगदान कर सकता है।"
                ),

                "favorable_conditions": (
                    "गर्म, गीला और अधिक नमी वाला मौसम रोग के लिए "
                    "अनुकूल होता है। लगातार बारिश और लंबे समय तक "
                    "पत्तियों का गीला रहना रोग को तेजी से बढ़ा सकता है।"
                )
            },

            "actions": [
                (
                    "संक्रमित निचली पत्तियों और पुराने टमाटर के "
                    "पौधों के अवशेषों को हटाकर नष्ट करें।"
                ),
                (
                    "ऊपर से पानी देने से बचें, मिट्टी के छींटों को "
                    "रोकने के लिए मल्चिंग करें और पौधों के बीच हवा "
                    "का प्रवाह बढ़ाएं।"
                )
            ],

            # =================================================
            # MODERATE: 10% - <60%
            # =================================================

            "moderate_sprays": [
                {
                    "name": "Syngenta Kavach",
                    "active_ingredient": "Chlorothalonil 75% WP",
                    "instructions": (
                        "यह ब्रॉड-स्पेक्ट्रम कॉन्टैक्ट फंगीसाइड है। "
                        "BigHaat पर सामान्य मात्रा 1.25–2 ग्राम/लीटर "
                        "दी गई है। फसल-विशिष्ट लेबल मात्रा का पालन करें।"
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "kavach-fungicide?pf=search"
                    )
                },

                {
                    "name": "Blitox",
                    "active_ingredient": "Copper Oxychloride 50% WP",
                    "instructions": (
                        "यह सुरक्षात्मक कॉन्टैक्ट फंगीसाइड है। "
                        "टमाटर के लेबल पर लीफ स्पॉट के लिए अनुमति "
                        "होने पर उपयोग करें।"
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "tata-rallis-blitox-fungicide?pf=search"
                    )
                }
            ],

            # =================================================
            # HIGH: 60% - 100%
            # =================================================

            "high_sprays": [
                {
                    "name": "BASF Merivon",
                    "active_ingredient": (
                        "Fluxapyroxad 250 g/L + "
                        "Pyraclostrobin 250 g/L SC"
                    ),
                    "instructions": (
                        "BigHaat पर इसे विशेष रूप से टमाटर – "
                        "Early Blight और Septoria Leaf Spot के लिए "
                        "80–100 मिली प्रति एकड़, 200 लीटर पानी में "
                        "सूचीबद्ध किया गया है।"
                    ),
                    "url": (
                        "https://www.bighaat.com/products/"
                        "merivon-fungicide?pf=search"
                    )
                }
            ],

            "high_action": (
                "अधिक संक्रमण में छिड़काव के साथ अधिक संक्रमित "
                "पत्तियों को भी हटा दें। लेबल पर दिए गए स्प्रे "
                "अंतराल का पालन करें और जहां अनुमति हो वहां "
                "अलग-अलग mode-of-action वाले फंगीसाइड का "
                "रोटेशन करें।"
            ),

            "low_message": (
                "दिखाई देने वाला प्रभावित क्षेत्र 10% से कम है। "
                "इस अवस्था में स्प्रे की सलाह नहीं दी जाती। "
                "बचाव के उपाय अपनाएं और पौधे की नियमित निगरानी करें।"
            ),

            "warning": (
                "उत्पाद के लेबल पर दिए गए निर्देशों और स्थानीय "
                "कृषि विशेषज्ञों की सलाह का पालन करें।"
            )
        }
    }
}