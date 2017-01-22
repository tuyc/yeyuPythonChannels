import re
import os

def getprofileinfo(profile_path):
    #签名信息
    keystore_path = None
    storepassword = None
    alias = None
    with open(profile_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            pattern = re.compile('^#')
            if re.match(pattern, line) is None:
                kv = line.split("=")
                if 'key.store' == kv[0]:
                    keystore_path = kv[1].strip('\n')
                elif 'key.alias' == kv[0]:
                    alias = kv[1].strip('\n')
                elif 'key.alias.password' == kv[0]:
                    storepassword = kv[1].strip('\n')
    return keystore_path, alias, storepassword


def getapk(curdir):
    filepaths = os.listdir(curdir)
    for filepath in filepaths:
        if os.path.splitext(filepath)[1] == '.apk':
            return os.path.join(curdir, filepath)

    return None


def apkdecode(apkfile, inputfile):
    command = "apktool.sh d -f " + apkfile + " -o " + inputfile
    os.system(command)


def getchannels(channelfile):
    with open(channelfile, 'r') as f:
        lines = f.readlines()
        resultlines = []
        for line in lines:
            line = line.strip('\n')
            resultlines.append(line)
        return resultlines
    return None


def replace_mainfestchannel(mainfest, channel):
    with open(mainfest, 'r') as f:
        manifestTxt = f.read()
        result = replace_umengchannel(channel, manifestTxt)
    with open(mainfest, 'w') as f:
        f.write(result)

    with open(mainfest, 'r') as f:
        manifestTxt = f.read()
        result = replace_referrername(channel, manifestTxt)
    with open(mainfest, 'w') as f:
        f.write(result)


def replace_umengchannel(channel, manifest):
    pattern = r'(<meta-data\s+android:name="UMENG_CHANNEL"\s+android:value=")(\S+)("\s?/>)'
    replacement = r"\g<1>{channel}\g<3>".format(channel=channel)
    return re.sub(pattern, replacement, manifest)


def replace_referrername(channel, manifest):
    pattern = r'(<meta-data\s+android:name="REFERRER_NAME"\s+android:value=")(\S+)("\s?/>)'
    replacement = r"\g<1>{channel}\g<3>".format(channel=channel)
    return re.sub(pattern, replacement, manifest)


def build_unsigned_apk(builddir, apkfile):
    command = 'apktool.sh b ' + builddir + ' -o ' + apkfile
    os.system(command)
    return builddir.join(apkfile)


def jarsigner(keystore_path, storepassword, signedapk, unsignedapk, alias):
    command = "jarsigner -sigalg MD5withRSA -digestalg SHA1 -keystore " + keystore_path \
              + " -storepass " + storepassword + " -signedjar " + signedapk + " " + unsignedapk \
              + " " + alias
    os.system(command)


def manychannel_apk():
    # curdir = os.getcwd()
    curdir = '/Users/tuyc/Desktop/apktool/'
    (keystore_path, alias, storepassword) = getprofileinfo(os.path.join(curdir, 'local.properties'))
    builddir = os.path.join(curdir, 'build')
    if not os.path.exists(builddir):
        os.mkdir(builddir)
    channelfile = os.path.join(curdir, 'channel.txt')
    if not os.path.exists(channelfile):
        print('channel.txt not exist!')
        return None
    unsigneddir = os.path.join(curdir, 'unsigned')
    if not os.path.exists(unsigneddir):
        os.mkdir(unsigneddir)
    signeddir = os.path.join(curdir, 'signed')
    if not os.path.exists(signeddir):
        os.mkdir(signeddir)

    apkfile = getapk(curdir)
    if apkfile is None:
        print('no apk file!')
        return None

    apkdecode(apkfile, builddir)
    channels = getchannels(channelfile)
    if channels is None or len(channels) == 0:
        print('channel.txt have not channelinfo!')
        return None
    for channel in channels:
        manifest = os.path.join(builddir, 'AndroidManifest.xml')
        replace_mainfestchannel(manifest, channel)
        unsignedapk = os.path.join(unsigneddir, channel + '.apk')
        build_unsigned_apk(builddir, unsignedapk)
        signedapk = os.path.join(signeddir, channel + '.apk')
        jarsigner(keystore_path, storepassword, signedapk, unsignedapk, alias)


manychannel_apk()
