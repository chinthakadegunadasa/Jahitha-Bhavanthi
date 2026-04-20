# ජහිතා භවන්ති (Jahitha Bhavanthi)
## පංචස්කන්ධ පද්ධතිය විනිවිද දකින ඉංජිනේරුමය විග්‍රහයක්

මෙම ව්‍යාපෘතිය පංච උපාදානස්කන්ධය පිළිබඳ ඉංජිනේරුමය විග්‍රහය ඇතුළත් ග්‍රන්ථයේ නිල Repository එකයි. මෙය **GitOps** මූලධර්ම මත පදනම්ව ස්වයංක්‍රීයව (Automated CI/CD) ගොඩනැංවේ.

### 🛠 පද්ධති ව්‍යුහය (Architecture)
* **Format:** B5 (176mm x 250mm)
* **Processing:** Pandoc & Python-Docx
* **Workflow:** GitHub Actions මගින් සෑම `push` එකකදීම අලුත්ම පිටපත නිපදවයි.
* **Layout:** Full Justify & Auto-Hyphenation.

### 📂 ගොනු ව්‍යුහය
- `/src`: ග්‍රන්ථයේ පරිච්ඡේද (Markdown ගොනු).
- `/assets`: කවර සහ තාක්ෂණික රූපසටහන්.
- `/scripts`: ග්‍රන්ථය නිපදවීමට අවශ්‍ය Python කේත.
- `/output`: නිපදවන ලද අවසන් DOCX/PDF ගොනු.

### 🚀 භාවිතා කරන ආකාරය
1. `src/` ෆෝල්ඩරය තුළ ඇති පරිච්ඡේද සංස්කරණය කරන්න.
2. වෙනස්කම් `commit` කර `push` කරන්න.
3. **Actions** ටැබ් එක හරහා නවතම B5 Manuscript එක බාගත කරන්න.

### 🖋 කතෘ
**චින්තක දේශප්‍රිය ගුණදාස (Madduma Kattadilage Chinthaka Deshapriya Gunadasa)**
Chief Technology Officer (CTO) & CSI - Cybergate Services Private Limited.
Red Hat Certified Architect (RHCA).
