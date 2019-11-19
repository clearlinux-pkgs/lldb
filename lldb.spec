#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x0FC3042E345AD05D (hans@chromium.org)
#
Name     : lldb
Version  : 9.0.0
Release  : 3
URL      : http://releases.llvm.org/9.0.0/lldb-9.0.0.src.tar.xz
Source0  : http://releases.llvm.org/9.0.0/lldb-9.0.0.src.tar.xz
Source1 : http://releases.llvm.org/9.0.0/lldb-9.0.0.src.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 ISC MIT
Requires: lldb-bin = %{version}-%{release}
Requires: lldb-lib = %{version}-%{release}
Requires: lldb-license = %{version}-%{release}
Requires: lldb-python = %{version}-%{release}
Requires: lldb-python3 = %{version}-%{release}
Requires: ptyprocess
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : doxygen
BuildRequires : glibc-dev
BuildRequires : libxml2-dev
BuildRequires : llvm
BuildRequires : llvm-dev = %{version}
BuildRequires : ncurses-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libedit)
BuildRequires : ptyprocess
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : swig
Patch1: 0001-Fix-build-with-Python-support-find-intermediate-file.patch

%description
=================
LLDB Vim Frontend
=================
Prerequisites
-------------

%package bin
Summary: bin components for the lldb package.
Group: Binaries
Requires: lldb-license = %{version}-%{release}

%description bin
bin components for the lldb package.


%package dev
Summary: dev components for the lldb package.
Group: Development
Requires: lldb-lib = %{version}-%{release}
Requires: lldb-bin = %{version}-%{release}
Provides: lldb-devel = %{version}-%{release}
Requires: lldb = %{version}-%{release}

%description dev
dev components for the lldb package.


%package lib
Summary: lib components for the lldb package.
Group: Libraries
Requires: lldb-license = %{version}-%{release}

%description lib
lib components for the lldb package.


%package license
Summary: license components for the lldb package.
Group: Default

%description license
license components for the lldb package.


%package python
Summary: python components for the lldb package.
Group: Default
Requires: lldb-python3 = %{version}-%{release}

%description python
python components for the lldb package.


%package python3
Summary: python3 components for the lldb package.
Group: Default
Requires: python3-core

%description python3
python3 components for the lldb package.


%prep
%setup -q -n lldb-9.0.0.src
cd %{_builddir}/lldb-9.0.0.src
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574159502
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CC=clang
export CXX=clang++
export LD=ld.gold
CFLAGS=${CFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
CXXFLAGS=${CXXFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
unset LDFLAGS
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DCMAKE_C_FLAGS="`sed -E 's/-Wl,\S+\s//g; s/-Wp,-D_FORTIFY_SOURCE=2//' <<<$CFLAGS`" \
-DCMAKE_CXX_FLAGS="`sed -E 's/-Wl,\S+\s//g; s/-Wp,-D_FORTIFY_SOURCE=2//' <<<$CXXFLAGS`" \
-DLLVM_HOST_TRIPLE="x86_64-generic-linux" \
-DLLVM_LIBDIR_SUFFIX=64 \
-DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
-DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1574159502
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lldb
cp %{_builddir}/lldb-9.0.0.src/LICENSE.TXT %{buildroot}/usr/share/package-licenses/lldb/8af372ad1edbed2cfaf0e79d25f7136ec6e55b47
cp %{_builddir}/lldb-9.0.0.src/third_party/Python/module/pexpect-4.6/LICENSE %{buildroot}/usr/share/package-licenses/lldb/5a99e7077ee89ba92fb3f584855e8970096cd5dc
cp %{_builddir}/lldb-9.0.0.src/third_party/Python/module/ptyprocess-0.6.0/LICENSE %{buildroot}/usr/share/package-licenses/lldb/db1f866b29c6a191752c7c5924b7572cdbc47c34
cp %{_builddir}/lldb-9.0.0.src/third_party/Python/module/six/LICENSE %{buildroot}/usr/share/package-licenses/lldb/f226af67862c0c7a0e921e24672a3a1375691e3e
pushd clr-build
%make_install
popd
## install_append content
pushd %{buildroot}/usr
mkdir -p lib
mv lib64/python* lib
cd lib/python*/site-packages/lldb
rm _lldb.so
t=`readlink ../../../../lib64/liblldb.so`
ln -s ../../../../lib64/$t _lldb.so
popd
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lldb
/usr/bin/lldb-argdumper
/usr/bin/lldb-instr
/usr/bin/lldb-mi
/usr/bin/lldb-server
/usr/bin/lldb-vscode

%files dev
%defattr(-,root,root,-)
/usr/include/lldb/API/LLDB.h
/usr/include/lldb/API/SBAddress.h
/usr/include/lldb/API/SBAttachInfo.h
/usr/include/lldb/API/SBBlock.h
/usr/include/lldb/API/SBBreakpoint.h
/usr/include/lldb/API/SBBreakpointLocation.h
/usr/include/lldb/API/SBBreakpointName.h
/usr/include/lldb/API/SBBroadcaster.h
/usr/include/lldb/API/SBCommandInterpreter.h
/usr/include/lldb/API/SBCommandReturnObject.h
/usr/include/lldb/API/SBCommunication.h
/usr/include/lldb/API/SBCompileUnit.h
/usr/include/lldb/API/SBData.h
/usr/include/lldb/API/SBDebugger.h
/usr/include/lldb/API/SBDeclaration.h
/usr/include/lldb/API/SBDefines.h
/usr/include/lldb/API/SBError.h
/usr/include/lldb/API/SBEvent.h
/usr/include/lldb/API/SBExecutionContext.h
/usr/include/lldb/API/SBExpressionOptions.h
/usr/include/lldb/API/SBFileSpec.h
/usr/include/lldb/API/SBFileSpecList.h
/usr/include/lldb/API/SBFrame.h
/usr/include/lldb/API/SBFunction.h
/usr/include/lldb/API/SBHostOS.h
/usr/include/lldb/API/SBInstruction.h
/usr/include/lldb/API/SBInstructionList.h
/usr/include/lldb/API/SBLanguageRuntime.h
/usr/include/lldb/API/SBLaunchInfo.h
/usr/include/lldb/API/SBLineEntry.h
/usr/include/lldb/API/SBListener.h
/usr/include/lldb/API/SBMemoryRegionInfo.h
/usr/include/lldb/API/SBMemoryRegionInfoList.h
/usr/include/lldb/API/SBModule.h
/usr/include/lldb/API/SBModuleSpec.h
/usr/include/lldb/API/SBPlatform.h
/usr/include/lldb/API/SBProcess.h
/usr/include/lldb/API/SBProcessInfo.h
/usr/include/lldb/API/SBQueue.h
/usr/include/lldb/API/SBQueueItem.h
/usr/include/lldb/API/SBReproducer.h
/usr/include/lldb/API/SBSection.h
/usr/include/lldb/API/SBSourceManager.h
/usr/include/lldb/API/SBStream.h
/usr/include/lldb/API/SBStringList.h
/usr/include/lldb/API/SBStructuredData.h
/usr/include/lldb/API/SBSymbol.h
/usr/include/lldb/API/SBSymbolContext.h
/usr/include/lldb/API/SBSymbolContextList.h
/usr/include/lldb/API/SBTarget.h
/usr/include/lldb/API/SBThread.h
/usr/include/lldb/API/SBThreadCollection.h
/usr/include/lldb/API/SBThreadPlan.h
/usr/include/lldb/API/SBTrace.h
/usr/include/lldb/API/SBTraceOptions.h
/usr/include/lldb/API/SBType.h
/usr/include/lldb/API/SBTypeCategory.h
/usr/include/lldb/API/SBTypeEnumMember.h
/usr/include/lldb/API/SBTypeFilter.h
/usr/include/lldb/API/SBTypeFormat.h
/usr/include/lldb/API/SBTypeNameSpecifier.h
/usr/include/lldb/API/SBTypeSummary.h
/usr/include/lldb/API/SBTypeSynthetic.h
/usr/include/lldb/API/SBUnixSignals.h
/usr/include/lldb/API/SBValue.h
/usr/include/lldb/API/SBValueList.h
/usr/include/lldb/API/SBVariablesOptions.h
/usr/include/lldb/API/SBWatchpoint.h
/usr/include/lldb/Breakpoint/Breakpoint.h
/usr/include/lldb/Breakpoint/BreakpointID.h
/usr/include/lldb/Breakpoint/BreakpointIDList.h
/usr/include/lldb/Breakpoint/BreakpointList.h
/usr/include/lldb/Breakpoint/BreakpointLocation.h
/usr/include/lldb/Breakpoint/BreakpointLocationCollection.h
/usr/include/lldb/Breakpoint/BreakpointLocationList.h
/usr/include/lldb/Breakpoint/BreakpointName.h
/usr/include/lldb/Breakpoint/BreakpointOptions.h
/usr/include/lldb/Breakpoint/BreakpointPrecondition.h
/usr/include/lldb/Breakpoint/BreakpointResolver.h
/usr/include/lldb/Breakpoint/BreakpointResolverAddress.h
/usr/include/lldb/Breakpoint/BreakpointResolverFileLine.h
/usr/include/lldb/Breakpoint/BreakpointResolverFileRegex.h
/usr/include/lldb/Breakpoint/BreakpointResolverName.h
/usr/include/lldb/Breakpoint/BreakpointResolverScripted.h
/usr/include/lldb/Breakpoint/BreakpointSite.h
/usr/include/lldb/Breakpoint/BreakpointSiteList.h
/usr/include/lldb/Breakpoint/Stoppoint.h
/usr/include/lldb/Breakpoint/StoppointCallbackContext.h
/usr/include/lldb/Breakpoint/StoppointLocation.h
/usr/include/lldb/Breakpoint/Watchpoint.h
/usr/include/lldb/Breakpoint/WatchpointList.h
/usr/include/lldb/Breakpoint/WatchpointOptions.h
/usr/include/lldb/Core/Address.h
/usr/include/lldb/Core/AddressRange.h
/usr/include/lldb/Core/AddressResolver.h
/usr/include/lldb/Core/AddressResolverFileLine.h
/usr/include/lldb/Core/AddressResolverName.h
/usr/include/lldb/Core/Architecture.h
/usr/include/lldb/Core/ClangForward.h
/usr/include/lldb/Core/Communication.h
/usr/include/lldb/Core/Debugger.h
/usr/include/lldb/Core/Disassembler.h
/usr/include/lldb/Core/DumpDataExtractor.h
/usr/include/lldb/Core/DumpRegisterValue.h
/usr/include/lldb/Core/EmulateInstruction.h
/usr/include/lldb/Core/FileLineResolver.h
/usr/include/lldb/Core/FileSpecList.h
/usr/include/lldb/Core/FormatEntity.h
/usr/include/lldb/Core/Highlighter.h
/usr/include/lldb/Core/IOHandler.h
/usr/include/lldb/Core/IOStreamMacros.h
/usr/include/lldb/Core/LoadedModuleInfoList.h
/usr/include/lldb/Core/Mangled.h
/usr/include/lldb/Core/MappedHash.h
/usr/include/lldb/Core/Module.h
/usr/include/lldb/Core/ModuleChild.h
/usr/include/lldb/Core/ModuleList.h
/usr/include/lldb/Core/ModuleSpec.h
/usr/include/lldb/Core/Opcode.h
/usr/include/lldb/Core/PluginInterface.h
/usr/include/lldb/Core/PluginManager.h
/usr/include/lldb/Core/RichManglingContext.h
/usr/include/lldb/Core/STLUtils.h
/usr/include/lldb/Core/SearchFilter.h
/usr/include/lldb/Core/Section.h
/usr/include/lldb/Core/SourceManager.h
/usr/include/lldb/Core/StreamAsynchronousIO.h
/usr/include/lldb/Core/StreamBuffer.h
/usr/include/lldb/Core/StreamFile.h
/usr/include/lldb/Core/StructuredDataImpl.h
/usr/include/lldb/Core/ThreadSafeDenseMap.h
/usr/include/lldb/Core/ThreadSafeDenseSet.h
/usr/include/lldb/Core/ThreadSafeSTLMap.h
/usr/include/lldb/Core/ThreadSafeSTLVector.h
/usr/include/lldb/Core/ThreadSafeValue.h
/usr/include/lldb/Core/UniqueCStringMap.h
/usr/include/lldb/Core/UserSettingsController.h
/usr/include/lldb/Core/Value.h
/usr/include/lldb/Core/ValueObject.h
/usr/include/lldb/Core/ValueObjectCast.h
/usr/include/lldb/Core/ValueObjectChild.h
/usr/include/lldb/Core/ValueObjectConstResult.h
/usr/include/lldb/Core/ValueObjectConstResultCast.h
/usr/include/lldb/Core/ValueObjectConstResultChild.h
/usr/include/lldb/Core/ValueObjectConstResultImpl.h
/usr/include/lldb/Core/ValueObjectDynamicValue.h
/usr/include/lldb/Core/ValueObjectList.h
/usr/include/lldb/Core/ValueObjectMemory.h
/usr/include/lldb/Core/ValueObjectRegister.h
/usr/include/lldb/Core/ValueObjectSyntheticFilter.h
/usr/include/lldb/Core/ValueObjectVariable.h
/usr/include/lldb/Core/dwarf.h
/usr/include/lldb/DataFormatters/CXXFunctionPointer.h
/usr/include/lldb/DataFormatters/DataVisualization.h
/usr/include/lldb/DataFormatters/DumpValueObjectOptions.h
/usr/include/lldb/DataFormatters/FormatCache.h
/usr/include/lldb/DataFormatters/FormatClasses.h
/usr/include/lldb/DataFormatters/FormatManager.h
/usr/include/lldb/DataFormatters/FormattersContainer.h
/usr/include/lldb/DataFormatters/FormattersHelpers.h
/usr/include/lldb/DataFormatters/LanguageCategory.h
/usr/include/lldb/DataFormatters/StringPrinter.h
/usr/include/lldb/DataFormatters/TypeCategory.h
/usr/include/lldb/DataFormatters/TypeCategoryMap.h
/usr/include/lldb/DataFormatters/TypeFormat.h
/usr/include/lldb/DataFormatters/TypeSummary.h
/usr/include/lldb/DataFormatters/TypeSynthetic.h
/usr/include/lldb/DataFormatters/TypeValidator.h
/usr/include/lldb/DataFormatters/ValueObjectPrinter.h
/usr/include/lldb/DataFormatters/VectorIterator.h
/usr/include/lldb/DataFormatters/VectorType.h
/usr/include/lldb/Expression/DWARFExpression.h
/usr/include/lldb/Expression/DiagnosticManager.h
/usr/include/lldb/Expression/DynamicCheckerFunctions.h
/usr/include/lldb/Expression/Expression.h
/usr/include/lldb/Expression/ExpressionParser.h
/usr/include/lldb/Expression/ExpressionSourceCode.h
/usr/include/lldb/Expression/ExpressionTypeSystemHelper.h
/usr/include/lldb/Expression/ExpressionVariable.h
/usr/include/lldb/Expression/FunctionCaller.h
/usr/include/lldb/Expression/IRExecutionUnit.h
/usr/include/lldb/Expression/IRInterpreter.h
/usr/include/lldb/Expression/IRMemoryMap.h
/usr/include/lldb/Expression/LLVMUserExpression.h
/usr/include/lldb/Expression/Materializer.h
/usr/include/lldb/Expression/REPL.h
/usr/include/lldb/Expression/UserExpression.h
/usr/include/lldb/Expression/UtilityFunction.h
/usr/include/lldb/Host/Config.h
/usr/include/lldb/Host/ConnectionFileDescriptor.h
/usr/include/lldb/Host/Debug.h
/usr/include/lldb/Host/Editline.h
/usr/include/lldb/Host/File.h
/usr/include/lldb/Host/FileAction.h
/usr/include/lldb/Host/FileCache.h
/usr/include/lldb/Host/FileSystem.h
/usr/include/lldb/Host/Host.h
/usr/include/lldb/Host/HostGetOpt.h
/usr/include/lldb/Host/HostInfo.h
/usr/include/lldb/Host/HostInfoBase.h
/usr/include/lldb/Host/HostNativeProcess.h
/usr/include/lldb/Host/HostNativeProcessBase.h
/usr/include/lldb/Host/HostNativeThread.h
/usr/include/lldb/Host/HostNativeThreadBase.h
/usr/include/lldb/Host/HostNativeThreadForward.h
/usr/include/lldb/Host/HostProcess.h
/usr/include/lldb/Host/HostThread.h
/usr/include/lldb/Host/LockFile.h
/usr/include/lldb/Host/LockFileBase.h
/usr/include/lldb/Host/MainLoop.h
/usr/include/lldb/Host/MainLoopBase.h
/usr/include/lldb/Host/MonitoringProcessLauncher.h
/usr/include/lldb/Host/OptionParser.h
/usr/include/lldb/Host/Pipe.h
/usr/include/lldb/Host/PipeBase.h
/usr/include/lldb/Host/PosixApi.h
/usr/include/lldb/Host/ProcessLaunchInfo.h
/usr/include/lldb/Host/ProcessLauncher.h
/usr/include/lldb/Host/ProcessRunLock.h
/usr/include/lldb/Host/PseudoTerminal.h
/usr/include/lldb/Host/SafeMachO.h
/usr/include/lldb/Host/Socket.h
/usr/include/lldb/Host/SocketAddress.h
/usr/include/lldb/Host/StringConvert.h
/usr/include/lldb/Host/TaskPool.h
/usr/include/lldb/Host/Terminal.h
/usr/include/lldb/Host/ThreadLauncher.h
/usr/include/lldb/Host/Time.h
/usr/include/lldb/Host/XML.h
/usr/include/lldb/Host/android/HostInfoAndroid.h
/usr/include/lldb/Host/common/GetOptInc.h
/usr/include/lldb/Host/common/NativeBreakpointList.h
/usr/include/lldb/Host/common/NativeProcessProtocol.h
/usr/include/lldb/Host/common/NativeRegisterContext.h
/usr/include/lldb/Host/common/NativeThreadProtocol.h
/usr/include/lldb/Host/common/NativeWatchpointList.h
/usr/include/lldb/Host/common/TCPSocket.h
/usr/include/lldb/Host/common/UDPSocket.h
/usr/include/lldb/Host/freebsd/HostInfoFreeBSD.h
/usr/include/lldb/Host/linux/AbstractSocket.h
/usr/include/lldb/Host/linux/HostInfoLinux.h
/usr/include/lldb/Host/linux/Ptrace.h
/usr/include/lldb/Host/linux/Support.h
/usr/include/lldb/Host/linux/Uio.h
/usr/include/lldb/Host/macosx/HostInfoMacOSX.h
/usr/include/lldb/Host/macosx/HostThreadMacOSX.h
/usr/include/lldb/Host/netbsd/HostInfoNetBSD.h
/usr/include/lldb/Host/openbsd/HostInfoOpenBSD.h
/usr/include/lldb/Host/posix/ConnectionFileDescriptorPosix.h
/usr/include/lldb/Host/posix/DomainSocket.h
/usr/include/lldb/Host/posix/Fcntl.h
/usr/include/lldb/Host/posix/HostInfoPosix.h
/usr/include/lldb/Host/posix/HostProcessPosix.h
/usr/include/lldb/Host/posix/HostThreadPosix.h
/usr/include/lldb/Host/posix/LockFilePosix.h
/usr/include/lldb/Host/posix/PipePosix.h
/usr/include/lldb/Host/posix/ProcessLauncherPosixFork.h
/usr/include/lldb/Host/windows/AutoHandle.h
/usr/include/lldb/Host/windows/ConnectionGenericFileWindows.h
/usr/include/lldb/Host/windows/HostInfoWindows.h
/usr/include/lldb/Host/windows/HostProcessWindows.h
/usr/include/lldb/Host/windows/HostThreadWindows.h
/usr/include/lldb/Host/windows/LockFileWindows.h
/usr/include/lldb/Host/windows/PipeWindows.h
/usr/include/lldb/Host/windows/PosixApi.h
/usr/include/lldb/Host/windows/ProcessLauncherWindows.h
/usr/include/lldb/Host/windows/editlinewin.h
/usr/include/lldb/Host/windows/windows.h
/usr/include/lldb/Initialization/SystemInitializer.h
/usr/include/lldb/Initialization/SystemInitializerCommon.h
/usr/include/lldb/Initialization/SystemLifetimeManager.h
/usr/include/lldb/Interpreter/CommandAlias.h
/usr/include/lldb/Interpreter/CommandCompletions.h
/usr/include/lldb/Interpreter/CommandHistory.h
/usr/include/lldb/Interpreter/CommandInterpreter.h
/usr/include/lldb/Interpreter/CommandObject.h
/usr/include/lldb/Interpreter/CommandObjectMultiword.h
/usr/include/lldb/Interpreter/CommandObjectRegexCommand.h
/usr/include/lldb/Interpreter/CommandOptionValidators.h
/usr/include/lldb/Interpreter/CommandReturnObject.h
/usr/include/lldb/Interpreter/OptionArgParser.h
/usr/include/lldb/Interpreter/OptionGroupArchitecture.h
/usr/include/lldb/Interpreter/OptionGroupBoolean.h
/usr/include/lldb/Interpreter/OptionGroupFile.h
/usr/include/lldb/Interpreter/OptionGroupFormat.h
/usr/include/lldb/Interpreter/OptionGroupOutputFile.h
/usr/include/lldb/Interpreter/OptionGroupPlatform.h
/usr/include/lldb/Interpreter/OptionGroupString.h
/usr/include/lldb/Interpreter/OptionGroupUInt64.h
/usr/include/lldb/Interpreter/OptionGroupUUID.h
/usr/include/lldb/Interpreter/OptionGroupValueObjectDisplay.h
/usr/include/lldb/Interpreter/OptionGroupVariable.h
/usr/include/lldb/Interpreter/OptionGroupWatchpoint.h
/usr/include/lldb/Interpreter/OptionValue.h
/usr/include/lldb/Interpreter/OptionValueArch.h
/usr/include/lldb/Interpreter/OptionValueArgs.h
/usr/include/lldb/Interpreter/OptionValueArray.h
/usr/include/lldb/Interpreter/OptionValueBoolean.h
/usr/include/lldb/Interpreter/OptionValueChar.h
/usr/include/lldb/Interpreter/OptionValueDictionary.h
/usr/include/lldb/Interpreter/OptionValueEnumeration.h
/usr/include/lldb/Interpreter/OptionValueFileSpec.h
/usr/include/lldb/Interpreter/OptionValueFileSpecList.h
/usr/include/lldb/Interpreter/OptionValueFormat.h
/usr/include/lldb/Interpreter/OptionValueFormatEntity.h
/usr/include/lldb/Interpreter/OptionValueLanguage.h
/usr/include/lldb/Interpreter/OptionValuePathMappings.h
/usr/include/lldb/Interpreter/OptionValueProperties.h
/usr/include/lldb/Interpreter/OptionValueRegex.h
/usr/include/lldb/Interpreter/OptionValueSInt64.h
/usr/include/lldb/Interpreter/OptionValueString.h
/usr/include/lldb/Interpreter/OptionValueUInt64.h
/usr/include/lldb/Interpreter/OptionValueUUID.h
/usr/include/lldb/Interpreter/OptionValues.h
/usr/include/lldb/Interpreter/Options.h
/usr/include/lldb/Interpreter/Property.h
/usr/include/lldb/Interpreter/ScriptInterpreter.h
/usr/include/lldb/Symbol/ArmUnwindInfo.h
/usr/include/lldb/Symbol/Block.h
/usr/include/lldb/Symbol/ClangASTContext.h
/usr/include/lldb/Symbol/ClangASTImporter.h
/usr/include/lldb/Symbol/ClangExternalASTSourceCallbacks.h
/usr/include/lldb/Symbol/ClangExternalASTSourceCommon.h
/usr/include/lldb/Symbol/ClangUtil.h
/usr/include/lldb/Symbol/CompactUnwindInfo.h
/usr/include/lldb/Symbol/CompileUnit.h
/usr/include/lldb/Symbol/CompilerDecl.h
/usr/include/lldb/Symbol/CompilerDeclContext.h
/usr/include/lldb/Symbol/CompilerType.h
/usr/include/lldb/Symbol/CxxModuleHandler.h
/usr/include/lldb/Symbol/DWARFCallFrameInfo.h
/usr/include/lldb/Symbol/DebugMacros.h
/usr/include/lldb/Symbol/DeclVendor.h
/usr/include/lldb/Symbol/Declaration.h
/usr/include/lldb/Symbol/FuncUnwinders.h
/usr/include/lldb/Symbol/Function.h
/usr/include/lldb/Symbol/LineEntry.h
/usr/include/lldb/Symbol/LineTable.h
/usr/include/lldb/Symbol/LocateSymbolFile.h
/usr/include/lldb/Symbol/ObjectContainer.h
/usr/include/lldb/Symbol/ObjectFile.h
/usr/include/lldb/Symbol/PostfixExpression.h
/usr/include/lldb/Symbol/SourceModule.h
/usr/include/lldb/Symbol/Symbol.h
/usr/include/lldb/Symbol/SymbolContext.h
/usr/include/lldb/Symbol/SymbolContextScope.h
/usr/include/lldb/Symbol/SymbolFile.h
/usr/include/lldb/Symbol/SymbolVendor.h
/usr/include/lldb/Symbol/Symtab.h
/usr/include/lldb/Symbol/TaggedASTType.h
/usr/include/lldb/Symbol/Type.h
/usr/include/lldb/Symbol/TypeList.h
/usr/include/lldb/Symbol/TypeMap.h
/usr/include/lldb/Symbol/TypeSystem.h
/usr/include/lldb/Symbol/UnwindPlan.h
/usr/include/lldb/Symbol/UnwindTable.h
/usr/include/lldb/Symbol/Variable.h
/usr/include/lldb/Symbol/VariableList.h
/usr/include/lldb/Symbol/VerifyDecl.h
/usr/include/lldb/Target/ABI.h
/usr/include/lldb/Target/DynamicLoader.h
/usr/include/lldb/Target/ExecutionContext.h
/usr/include/lldb/Target/ExecutionContextScope.h
/usr/include/lldb/Target/InstrumentationRuntime.h
/usr/include/lldb/Target/InstrumentationRuntimeStopInfo.h
/usr/include/lldb/Target/JITLoader.h
/usr/include/lldb/Target/JITLoaderList.h
/usr/include/lldb/Target/Language.h
/usr/include/lldb/Target/LanguageRuntime.h
/usr/include/lldb/Target/Memory.h
/usr/include/lldb/Target/MemoryHistory.h
/usr/include/lldb/Target/MemoryRegionInfo.h
/usr/include/lldb/Target/ModuleCache.h
/usr/include/lldb/Target/OperatingSystem.h
/usr/include/lldb/Target/PathMappingList.h
/usr/include/lldb/Target/Platform.h
/usr/include/lldb/Target/Process.h
/usr/include/lldb/Target/ProcessStructReader.h
/usr/include/lldb/Target/Queue.h
/usr/include/lldb/Target/QueueItem.h
/usr/include/lldb/Target/QueueList.h
/usr/include/lldb/Target/RegisterCheckpoint.h
/usr/include/lldb/Target/RegisterContext.h
/usr/include/lldb/Target/RegisterNumber.h
/usr/include/lldb/Target/RemoteAwarePlatform.h
/usr/include/lldb/Target/SectionLoadHistory.h
/usr/include/lldb/Target/SectionLoadList.h
/usr/include/lldb/Target/StackFrame.h
/usr/include/lldb/Target/StackFrameList.h
/usr/include/lldb/Target/StackFrameRecognizer.h
/usr/include/lldb/Target/StackID.h
/usr/include/lldb/Target/StopInfo.h
/usr/include/lldb/Target/StructuredDataPlugin.h
/usr/include/lldb/Target/SystemRuntime.h
/usr/include/lldb/Target/Target.h
/usr/include/lldb/Target/TargetList.h
/usr/include/lldb/Target/Thread.h
/usr/include/lldb/Target/ThreadCollection.h
/usr/include/lldb/Target/ThreadList.h
/usr/include/lldb/Target/ThreadPlan.h
/usr/include/lldb/Target/ThreadPlanBase.h
/usr/include/lldb/Target/ThreadPlanCallFunction.h
/usr/include/lldb/Target/ThreadPlanCallFunctionUsingABI.h
/usr/include/lldb/Target/ThreadPlanCallOnFunctionExit.h
/usr/include/lldb/Target/ThreadPlanCallUserExpression.h
/usr/include/lldb/Target/ThreadPlanPython.h
/usr/include/lldb/Target/ThreadPlanRunToAddress.h
/usr/include/lldb/Target/ThreadPlanShouldStopHere.h
/usr/include/lldb/Target/ThreadPlanStepInRange.h
/usr/include/lldb/Target/ThreadPlanStepInstruction.h
/usr/include/lldb/Target/ThreadPlanStepOut.h
/usr/include/lldb/Target/ThreadPlanStepOverBreakpoint.h
/usr/include/lldb/Target/ThreadPlanStepOverRange.h
/usr/include/lldb/Target/ThreadPlanStepRange.h
/usr/include/lldb/Target/ThreadPlanStepThrough.h
/usr/include/lldb/Target/ThreadPlanStepUntil.h
/usr/include/lldb/Target/ThreadPlanTracer.h
/usr/include/lldb/Target/ThreadSpec.h
/usr/include/lldb/Target/UnixSignals.h
/usr/include/lldb/Target/Unwind.h
/usr/include/lldb/Target/UnwindAssembly.h
/usr/include/lldb/Utility/AnsiTerminal.h
/usr/include/lldb/Utility/ArchSpec.h
/usr/include/lldb/Utility/Args.h
/usr/include/lldb/Utility/Baton.h
/usr/include/lldb/Utility/Broadcaster.h
/usr/include/lldb/Utility/CleanUp.h
/usr/include/lldb/Utility/CompletionRequest.h
/usr/include/lldb/Utility/Connection.h
/usr/include/lldb/Utility/ConstString.h
/usr/include/lldb/Utility/DataBuffer.h
/usr/include/lldb/Utility/DataBufferHeap.h
/usr/include/lldb/Utility/DataBufferLLVM.h
/usr/include/lldb/Utility/DataEncoder.h
/usr/include/lldb/Utility/DataExtractor.h
/usr/include/lldb/Utility/Endian.h
/usr/include/lldb/Utility/Environment.h
/usr/include/lldb/Utility/Event.h
/usr/include/lldb/Utility/FileCollector.h
/usr/include/lldb/Utility/FileSpec.h
/usr/include/lldb/Utility/Flags.h
/usr/include/lldb/Utility/IOObject.h
/usr/include/lldb/Utility/Iterable.h
/usr/include/lldb/Utility/JSON.h
/usr/include/lldb/Utility/LLDBAssert.h
/usr/include/lldb/Utility/Listener.h
/usr/include/lldb/Utility/Log.h
/usr/include/lldb/Utility/Logging.h
/usr/include/lldb/Utility/NameMatches.h
/usr/include/lldb/Utility/Predicate.h
/usr/include/lldb/Utility/ProcessInfo.h
/usr/include/lldb/Utility/RangeMap.h
/usr/include/lldb/Utility/RegisterValue.h
/usr/include/lldb/Utility/RegularExpression.h
/usr/include/lldb/Utility/Reproducer.h
/usr/include/lldb/Utility/ReproducerInstrumentation.h
/usr/include/lldb/Utility/Scalar.h
/usr/include/lldb/Utility/SelectHelper.h
/usr/include/lldb/Utility/SharedCluster.h
/usr/include/lldb/Utility/SharingPtr.h
/usr/include/lldb/Utility/State.h
/usr/include/lldb/Utility/Status.h
/usr/include/lldb/Utility/Stream.h
/usr/include/lldb/Utility/StreamCallback.h
/usr/include/lldb/Utility/StreamGDBRemote.h
/usr/include/lldb/Utility/StreamString.h
/usr/include/lldb/Utility/StreamTee.h
/usr/include/lldb/Utility/StringExtractor.h
/usr/include/lldb/Utility/StringExtractorGDBRemote.h
/usr/include/lldb/Utility/StringLexer.h
/usr/include/lldb/Utility/StringList.h
/usr/include/lldb/Utility/StructuredData.h
/usr/include/lldb/Utility/TildeExpressionResolver.h
/usr/include/lldb/Utility/Timeout.h
/usr/include/lldb/Utility/Timer.h
/usr/include/lldb/Utility/TraceOptions.h
/usr/include/lldb/Utility/UUID.h
/usr/include/lldb/Utility/UriParser.h
/usr/include/lldb/Utility/UserID.h
/usr/include/lldb/Utility/UserIDResolver.h
/usr/include/lldb/Utility/VASPrintf.h
/usr/include/lldb/Utility/VMRange.h
/usr/include/lldb/lldb-defines.h
/usr/include/lldb/lldb-enumerations.h
/usr/include/lldb/lldb-forward.h
/usr/include/lldb/lldb-private-defines.h
/usr/include/lldb/lldb-private-enumerations.h
/usr/include/lldb/lldb-private-forward.h
/usr/include/lldb/lldb-private-interfaces.h
/usr/include/lldb/lldb-private-types.h
/usr/include/lldb/lldb-private.h
/usr/include/lldb/lldb-public.h
/usr/include/lldb/lldb-types.h
/usr/include/lldb/lldb-versioning.h
/usr/lib64/liblldb.so
/usr/lib64/liblldbIntelFeatures.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblldb.so.9
/usr/lib64/liblldb.so.9.0.0
/usr/lib64/liblldbIntelFeatures.so.9

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lldb/5a99e7077ee89ba92fb3f584855e8970096cd5dc
/usr/share/package-licenses/lldb/8af372ad1edbed2cfaf0e79d25f7136ec6e55b47
/usr/share/package-licenses/lldb/db1f866b29c6a191752c7c5924b7572cdbc47c34
/usr/share/package-licenses/lldb/f226af67862c0c7a0e921e24672a3a1375691e3e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
