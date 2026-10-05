import numpy as np
from PIL import Image
import streamlit as st

# પેજ કન્ફિગરેશન
st.set_page_config(
    page_title="શ્રી બી. પી. અગ્રવાલ હાઇસ્કુલ, લીમડી",
    page_icon="🌿",
    layout="centered",
)

# હેડર સેક્શન
st.markdown(
    """
<div style='text-align: center; padding: 18px; background-color: #e8f5e9; border: 2px solid #1b4332; border-radius: 12px; margin-bottom: 20px;'>
    <h2 style='color: #1b4332; margin: 0; font-size: 22px; font-weight: bold;'>🏫 શાળાનું નામ: શ્રી બી. પી. અગ્રવાલ હાઇસ્કુલ, લીમડી</h2>
    <h4 style='color: #2d6a4f; margin: 8px 0 12px 0; font-size: 17px;'>🌱 AI પાક પર્ણ રોગ નિદાન અને સંકલિત વ્યવસ્થાપન સિસ્ટમ</h4>
    <div style='display: inline-block; background-color: #1b4332; color: #ffffff; padding: 6px 18px; border-radius: 16px; font-size: 14px; font-weight: bold;'>
        માર્ગદર્શક શ્રી નું નામ: ધીરેન્દ્ર પરમાર
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("📷 **કેમેરા સામે અસરગ્રસ્ત પાંદડું રાખી નીચે ફોટો ક્લિક કરો:**")

camera_photo = st.camera_input("પર્ણનું સ્કેનિંગ કરો")


def analyze_disease(img):
  """પર્ણ સ્પેક્ટ્રમ આધારે રોગનું સચોટ વૈજ્ઞાનિક વિશ્લેષણ"""
  img_rgb = img.convert("RGB")
  img_resized = img_rgb.resize((200, 200))
  arr = np.array(img_resized, dtype=np.float32)

  r = arr[:, :, 0]
  g = arr[:, :, 1]
  b = arr[:, :, 2]
  total = 200 * 200

  # કલર રેશિયો પૃથક્કરણ
  white_ratio = np.sum((r > 170) & (g > 170) & (b > 170)) / total
  rust_ratio = np.sum((r > 130) & (g < 110) & (b < 70)) / total
  yellow_ratio = np.sum((r > 140) & (g > 140) & (b < 100)) / total
  dark_ratio = np.sum((r < 75) & (g < 75) & (b < 75)) / total

  # ૧. પાવડરી મિલ્ડ્યુ (છારો રોગ)
  if white_ratio > 0.08:
    return {
        "name": "પાવડરી મિલ્ડ્યુ (છારો રોગ / Powdery Mildew)",
        "symptoms": (
            "પાંદડાની ઉપર તથા નીચેની સપાટી પર સફેદ રાખ અથવા લોટ જેવો સફેદ પાવડર"
            " જામી જાય છે. પ્રકાશસંશ્લેષણ અટકી જતાં પાંદડા પીળા પડીને સુકાઈ"
            " ખરી પડે છે."
        ),
        "chemical": (
            "હેક્ઝાકોનાઝોલ ૫% EC (Hexaconazole) અથવા ડીનોકેપ ૪૮% EC અથવા કાર્બેન્ડાઝીમ"
            " ૫૦% WP."
        ),
        "organic": (
            "ખાટી દેશી ગાયની છાશ (૧૫ દિવસ જૂની) અથવા લીમડાનું તેલ (Neem oil - ૧૫૦૦"
            " PPM)."
        ),
        "dosage": (
            "૧૫ લિટરના પંપમાં: રાસાયણિક ઉપચાર માટે હેક્ઝાકોનાઝોલ ૧૫ મિલી પાણીમાં"
            " ઉમેરી છાંટવું. દેશી ઉપચાર માટે ૫૦૦ મિલી ખાટી છાશ + ૫૦ મિલી લીમડાનું"
            " તેલ ૧૫ લિટર પાણીમાં સ્ટીકર (Sticker/Spreader) સાથે મિશ્ર કરી પર્ણ"
            " ભીંજાય તે રીતે છાંટવું."
        ),
        "time": (
            "સવારે ૭ થી ૧૦ વાગ્યા દરમિયાન અથવા સાંજે ૪ વાગ્યા પછી સૂર્યપ્રકાશ ધીમો"
            " હોય ત્યારે."
        ),
        "recovery": (
            "અંદાજે ૫ થી ૭ દિવસમાં નવી ફૂગ અટકી જશે અને ૭ મા દિવસે જરૂર જણાય તો"
            " બીજો હળવો છંટકાવ કરવો."
        ),
    }

  # ૨. રસ્ટ (ગેરુ રોગ)
  elif rust_ratio > 0.05:
    return {
        "name": "પાનનો ગેરુ / રસ્ટ રોગ (Common Rust)",
        "symptoms": (
            "પાંદડાની બંને સપાટી પર ઈંટ જેવા લાલાશ પડતા બદામી રંગના ઉપસેલા નાના"
            " ફોલ્લા (Pustules) બને છે, જેને અડકવાથી આંગળી પર કાટ જેવો પાવડર ચોંટે"
            " છે."
        ),
        "chemical": (
            "પ્રોપીકોનાઝોલ ૨૫% EC (Tilt) અથવા મેન્કોઝેબ ૭૫% WP (Dithane M-45)."
        ),
        "organic": (
            "ટ્રાઇકોડર્મા હાર્ઝિયાનમ (Trichoderma viride) જૈવિક ફૂગનાશક અથવા ગૌમૂત્ર"
            " અર્ક."
        ),
        "dosage": (
            "૧૫ લિટરના પંપમાં: પ્રોપીકોનાઝોલ ૧૫ મિલી અથવા મેન્કોઝેબ ૩૫ ગ્રામ પાણીમાં"
            " ઓગાળીને છાંટવું. જૈવિક ઉપચાર માટે ટ્રાઇકોડર્મા ૫૦ ગ્રામ ૧૫ લિટર"
            " પાણીમાં ગૂળના દ્રાવણ સાથે ઉમેરી છાંટવું."
        ),
        "time": "સવારના સમયે ઝાકળ ઉડી ગયા બાદ (સવારે ૮:૩૦ થી ૧૧:૦૦ વાગ્યા વચ્ચે).",
        "recovery": (
            "૬ થી ૮ દિવસમાં રસ્ટના બીજાણુઓ નિષ્ક્રિય બને છે; ૧૦ માં દિવસે પાક"
            " સ્વસ્થતા તરફ વળે છે."
        ),
    }

  # ૩. અર્લી બ્લાઇટ (સુકારો)
  elif dark_ratio > 0.06 and yellow_ratio > 0.08:
    return {
        "name": "અર્લી બ્લાઇટ / વહેલો સુકારો (Early Blight)",
        "symptoms": (
            "પાંદડા પર ઘેરા બદામી કે કાળા રંગના એકાંતરે ગોળાકાર વલયો (Target board"
            " જેવા ચકતા) પડે છે અને ફરતે પીળી કિનારી જોવા મળે છે."
        ),
        "chemical": (
            "કોપર ઓક્સીક્લોરાઇડ ૫૦% WP (COC) અથવા ક્લોરોથેલોનીલ ૭૫% WP અથવા ટેબુકોનાઝોલ."
        ),
        "organic": (
            "દસપર્ણી અર્ક અથવા ટ્રાઇકોડર્મા વિરીડી સાથે લીમડાના તેલનું સંયોજન."
        ),
        "dosage": (
            "૧૫ લિટરના પંપમાં: કોપર ઓક્સીક્લોરાઇડ ૪૦ ગ્રામ પાણીમાં યોગ્ય રીતે"
            " ઓગાળીને છાંટવું. દેશી માટે ૧ લિટર દસપર્ણી અર્ક ૧૫ લિટર પાણીમાં ગાળીને"
            " પર્ણની બંને બાજુ છંટકાવ કરવો."
        ),
        "time": "સાંજના ૪:૩૦ પછી વાતાવરણ ઠંડુ પડે ત્યારે.",
        "recovery": (
            "૭ થી ૧૦ દિવસમાં રોગનો ફેલાવો અટકે છે. ગંભીર સ્થિતિમાં ૮ મા દિવસે"
            " રીપીટ છંટકાવ અનિવાર્ય છે."
        ),
    }

  # ૪. લીફ કર્લ / મોઝેક વાયરસ (કોકડવા)
  elif yellow_ratio > 0.12:
    return {
        "name": "લીફ કર્લ / મોઝેક વાયરસ (કોકડવા રોગ)",
        "symptoms": (
            "પાંદડા અંદર અથવા બહારની તરફ હોડી આકારે વળી જવા, નસો જાડી થઈ ઉપસી"
            " આવવી અને છોડનો વિકાસ અટકીને વામન (Stunted) થઈ જવો."
        ),
        "chemical": (
            "વાહક સફેદ માખી/થ્રિપ્સ નિયંત્રણ માટે: એસીટામિપ્રિડ ૨૦% SP અથવા"
            " ડાયફેન્થિયુરોન ૫૦% WP અથવા ઇમિડાક્લોપ્રિડ ૧૭.૮% SL."
        ),
        "organic": (
            "પીળા અને વાદળી ચીકણા ટ્રેપ (Sticky Traps) પ્રતિ વીઘે ૮ નંગ + અગ્નિઅસ્ત્ર"
            " અથવા લીંબોળીનું તેલ (૫ મિલી/લિટર)."
        ),
        "dosage": (
            "૧૫ લિટરના પંપમાં: એસીટામિપ્રિડ ૮ ગ્રામ અથવા ઇમિડાક્લોપ્રિડ ૫ મિલી"
            " પાણીમાં ઉમેરીને છાંટવું. દેશી ઉપચારમાં ૫૦૦ મિલી અગ્નિઅસ્ત્ર ૧૫ લિટર"
            " પાણીમાં ભેળવી પંપ કરવો."
        ),
        "time": (
            "સૂર્યોદય પછી વહેલી સવારે જ્યારે વાહક જીવાતો પાંદડા નીચે સ્થિર હોય"
            " ત્યારે."
        ),
        "recovery": (
            "વાયરસ ગ્રસ્ત પાન મૂળ સ્થિતિમાં નહીં આવે પરંતુ ૭ થી ૧૨ દિવસમાં નવો"
            " ફૂટાવ એકદમ તંદુરસ્ત અને લીલો આવશે."
        ),
    }

  # ૫. સાઇટ્રસ કેન્કર (ખારીયો)
  elif dark_ratio > 0.04:
    return {
        "name": "સાઇટ્રસ કેન્કર (ખારીયો રોગ / Citrus Canker)",
        "symptoms": (
            "પાંદડાની બંને બાજુ ઉપસેલા, ખરબચડા, બદામી જખમ જેવા ડાઘા અને તેની આસપાસ"
            " સ્પષ્ટ પીળું તેલિયું વલય (Yellow Halo) દેખાવું."
        ),
        "chemical": (
            "સ્ટ્રેપ્ટોસાયક્લીન (Streptocycline) ૯૦:૧૦ + કોપર ઓક્સીક્લોરાઇડ (COC)."
        ),
        "organic": (
            "૧% બોルドો મિશ્રણ (Bordeaux Mixture) અથવા તાજી છાશ અને હળદરનું"
            " મિશ્રણ."
        ),
        "dosage": (
            "૧૫ લિટરના પંપમાં: ૧.૫ ગ્રામ સ્ટ્રેપ્ટોસાયક્લીન પાઉડર + ૩૦ ગ્રામ કોપર"
            " ઓક્સીક્લોરાઇડ સાથે મિક્સ કરી પાંદડા પૂરેપૂરા ભીંજાય તે રીતે છાંટવું."
        ),
        "time": "બપોરના તડકા સિવાય સાંજના ૪ વાગ્યા પછી.",
        "recovery": (
            "૮ થી ૧૨ દિવસમાં બેક્ટેરિયાનો ફેલાવો નિયંત્રિત થાય છે; ચોમાસામાં દર ૧૫"
            " દિવસે હળવો છંટકાવ ચાલુ રાખવો."
        ),
    }

  # સ્વસ્થ પાન
  else:
    return {
        "name": "તંદુરસ્ત પર્ણ (કોઈ ગંભીર રોગ નથી)",
        "symptoms": "પાંદડા પર કોઈ પ્રકારના ડાઘ, છારો કે સંકોચન જોવા મળતું નથી.",
        "chemical": "રાસાયણિક દવાની જરૂર નથી.",
        "organic": "સંરક્ષણાત્મક પગલાં તરીકે જીવામૃત અથવા પંચગવ્યનો છંટકાવ કરવો.",
        "dosage": "૧ લિટર જીવામૃત ૧૫ લિટર પાણીમાં ગાળીને સામાન્ય છંટકાવ કરવો.",
        "time": "કોઈપણ અનુકૂળ સમયે.",
        "recovery": "છોડ પહેલેથી જ સ્વસ્થ સ્થિતિમાં છે.",
    }


if camera_photo is not None:
  img = Image.open(camera_photo)
  res = analyze_disease(img)

  st.success("✅ પર્ણનું ડિજિટલ નિદાન પૂર્ણ થયું!")

  # ૭ મુદ્દાઓનું ક્રમબદ્ધ પ્રદર્શન
  st.markdown(f"### ૧. રોગનું ચોક્કસ નામ:\n**{res['name']}**")
  st.markdown(f"### ૨. રોગના ચોક્કસ લક્ષણો:\n{res['symptoms']}")
  st.markdown(f"### ૩. રાસાયણિક ઉપચાર:\n{res['chemical']}")
  st.markdown(f"### ૪. દેશી ઉપચાર:\n{res['organic']}")
  st.markdown(
      f"### ૫. ઉપચાર માટે દવાનો છંટકાવ (પ્રમાણ અને રીત):\n{res['dosage']}"
  )
  st.markdown(f"### ૬. કયા સમયે છંટકાવ કરવો:\n{res['time']}")
  st.markdown(f"### ૭. અંદાજે રોગ નિવારણ સમયગાળો:\n{res['recovery']}")

  # સ્પીચ ટેક્સ્ટ
  speech_clean = (
      f"રોગનું નામ: {res['name']}. "
      f"રાસાયણિક ઉપચાર: {res['chemical']}. "
      f"દેશી ઉપચાર: {res['organic']}. "
      f"દવાનું પ્રમાણ: {res['dosage']}. "
      f"છંટકાવ સમય: {res['time']}. "
      f"નિવારણ સમયગાળો: {res['recovery']}."
  )
  speech_clean = (
      speech_clean.replace('"', "")
      .replace("'", "")
      .replace("\n", " ")
      .replace("%", " ટકા ")
  )

  # Text-to-Speech HTML (માત્ર બટન ક્લિક કરવા પર જ બોલશે)
  tts_html = f"""
    <div style='margin-top: 25px; padding: 10px; background-color: #f1f8e9; border-radius: 10px; text-align: center;'>
        <button id="speakBtn" onclick="runSpeech()" style="background-color: #1b4332; color: #ffffff; border: none; padding: 12px 24px; border-radius: 8px; font-size: 16px; font-weight: bold; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            🔊 સંપૂર્ણ રિપોર્ટ ગુજરાતીમાં સાંભળો (Speak Report)
        </button>
    </div>
    <script>
        function runSpeech() {{
            window.speechSynthesis.cancel();
            var text = "{speech_clean}";
            var msg = new SpeechSynthesisUtterance(text);
            msg.lang = 'gu-IN';
            msg.rate = 0.9;
            window.speechSynthesis.speak(msg);
        }}
    </script>
    """
  st.components.v1.html(tts_html, height=90)

# ક્રેડિટ ફૂટર
st.markdown("---")
st.markdown(
    """
<div style='text-align: center; color: #333; font-size: 13px; line-height: 1.6;'>
    <b>શાળાનું નામ:</b> શ્રી બી. પી. અગ્રવાલ હાઇસ્કુલ, લીમડી<br>
    <b>માર્ગદર્શક શ્રી નું નામ:</b> ધીરેન્દ્ર પરમાર
</div>
""",
    unsafe_allow_html=True,
)
