import numpy as np
from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="શ્રી બી. પી. અગ્રવાલ હાઇસ્કુલ, લીમડી",
    page_icon="🌿",
    layout="centered",
)

# હેડર - શાળા અને માર્ગદર્શક શ્રી નું નામ
st.markdown(
    """
<div style='text-align: center; padding: 18px; background-color: #e8f5e9; border: 2px solid #1b4332; border-radius: 12px; margin-bottom: 20px;'>
    <h2 style='color: #1b4332; margin: 0; font-size: 22px; font-weight: bold;'>🏫 શાળાનું નામ: શ્રી બી. પી. અગ્રવાલ હાઇસ્કુલ, લીમડી</h2>
    <h4 style='color: #2d6a4f; margin: 8px 0 12px 0; font-size: 17px;'>🌱 AI વનસ્પતિ પર્ણ રોગ નિદાન સોફ્ટવેર</h4>
    <div style='display: inline-block; background-color: #1b4332; color: #ffffff; padding: 6px 18px; border-radius: 16px; font-size: 14px; font-weight: bold;'>
        માર્ગદર્શક શ્રી નું નામ: ધીરેન્દ્ર પરમાર
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("📷 નીચે કેમેરાથી પાંદડાનો ફોટો ક્લિક કરો, તુરંત ૧ સેકન્ડમાં વિશ્લેષણ મળશે:")

# સીધો લાઈવ કેમેરા ઓપન રાખવા માટે camera_input
camera_photo = st.camera_input("કેમેરા સામે પાંદડું લાવી ફોટો ક્લિક કરો")


def analyze_leaf_image(img):
  img_rgb = img.convert("RGB")
  img_resized = img_rgb.resize((200, 200))
  arr = np.array(img_resized, dtype=np.float32)

  r = arr[:, :, 0]
  g = arr[:, :, 1]
  b = arr[:, :, 2]
  total_pixels = 200 * 200

  # કલર સ્પેક્ટ્રમ રેશિયો
  white_ratio = np.sum((r > 170) & (g > 170) & (b > 170)) / total_pixels
  rust_ratio = np.sum((r > 130) & (g < 110) & (b < 70)) / total_pixels
  yellow_ratio = np.sum((r > 140) & (g > 140) & (b < 100)) / total_pixels
  dark_ratio = np.sum((r < 75) & (g < 75) & (b < 75)) / total_pixels

  if white_ratio > 0.08:
    crop = "ગુલાબ / ભીંડા / વેલાવાળા શાકભાજી"
    disease = "પાવડરી મિલ્ડ્યુ (છારો રોગ)"
    symptoms = "પાંદડાની સપાટી પર સફેદ લોટ જેવો પાવડર જામી જવો."
    cure = "ખાટી છાશ અથવા કાર્બેન્ડાઝીમ ફૂગનાશકનો છંટકાવ કરવો."
  elif rust_ratio > 0.05:
    crop = "મકાઈ / અનાજ પાક"
    disease = "પાનનો ગેરુ / રસ્ટ રોગ"
    symptoms = "પાંદડા પર ઈંટ જેવા લાલ-બદામી રંગના ઉપસેલા ફોલ્લા."
    cure = "ટ્રાઇકોડર્મા અથવા પ્રોપીકોનાઝોલનો છંટકાવ કરવો."
  elif dark_ratio > 0.06 and yellow_ratio > 0.08:
    crop = "ટામેટા / બટાટા"
    disease = "અર્લી બ્લાઇટ (વહેલો સુકારો)"
    symptoms = "પાંદડા પર બદામી-કાળા ગોળાકાર વલયો અને કિનારી પીળી પડવી."
    cure = "અસરગ્રસ્ત પાન દૂર કરવા અને મેન્કોઝેબનો છંટકાવ કરવો."
  elif yellow_ratio > 0.12:
    crop = "પપૈયા / મરચી / કપાસ"
    disease = "લીફ કર્લ / મોઝેક વાયરસ (કોકડવા રોગ)"
    symptoms = "પાંદડા કોકડાઈ જવા અને પીળી નસો દેખાવી."
    cure = "વાહક સફેદ માખી નિયંત્રણ માટે લીમડાનું તેલ છાંટવું."
  elif dark_ratio > 0.04:
    crop = "લીંબુ વર્ગના ફળો"
    disease = "સાઇટ્રસ કેન્કર (ખારીયો રોગ)"
    symptoms = "પાંદડા પર ખરબચડા બદામી રંગના ચાંઠા અને પીળી કિનારી."
    cure = "બોルドો મિશ્રણ અથવા કોપર ઓક્સીક્લોરાઇડનો છંટકાવ કરવો."
  else:
    crop = "સામાન્ય પાક"
    disease = "સ્વસ્થ પર્ણ"
    symptoms = "કોઈ ગંભીર રોગના લક્ષણ જણાતા નથી."
    cure = "નિયમિત સિંચાઈ અને સામાન્ય ખાતર પૂરતું છે."

  return crop, disease, symptoms, cure


if camera_photo is not None:
  img = Image.open(camera_photo)
  crop, disease, symptoms, cure = analyze_leaf_image(img)

  st.success("✅ ૧ સેકન્ડમાં વિશ્લેષણ પૂર્ણ!")
  st.markdown(f"### ૧. સંભવિત વનસ્પતિ / પાક: **{crop}**")
  st.markdown(f"### ૨. રોગનું નામ: **{disease}**")
  st.markdown(f"**૩. મુખ્ય લક્ષણ:** {symptoms}")
  st.markdown(f"**૪. તાત્કાલિક ઉપાય:** {cure}")

  # ઑડિયો સ્પીચ માટે વાક્ય
  speech_text = f"વનસ્પતિ {crop}. રોગનું નામ {disease}. ઉપાય {cure}"

  # બ્રાઉઝરનું Text-to-Speech ફીચર (ગુજરાતી / હિન્દી અવાજમાં બોલશે)
  tts_script = f"""
    <script>
        function speakReport() {{
            var msg = new SpeechSynthesisUtterance("{speech_text}");
            msg.lang = 'gu-IN';
            msg.rate = 0.95;
            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(msg);
        }}
        // આપોઆપ અથવા બટનથી બોલશે
        speakReport();
    </script>
    <div style='margin-top: 15px;'>
        <button onclick="speakReport()" style="background-color: #2d6a4f; color: white; border: none; padding: 10px 20px; border-radius: 8px; font-size: 15px; cursor: pointer; font-weight: bold;">
            🔊 ફરીથી ગુજરાતીમાં સાંભળો (Speak Report)
        </button>
    </div>
    """
  st.components.v1.html(tts_script, height=70)

# ફૂટર
st.markdown("---")
st.markdown(
    """
<div style='text-align: center; color: #444; font-size: 13px;'>
    <b>શાળાનું નામ:</b> શ્રી બી. પી. અગ્રવાલ હાઇસ્કુલ, લીમડી<br>
    <b>માર્ગદર્શક શ્રી નું નામ:</b> ધીરેન્દ્ર પરમાર
</div>
""",
    unsafe_allow_html=True,
)
